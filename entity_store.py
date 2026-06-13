import threading
import psycopg2
import psycopg2.pool
from config import settings

_pool: psycopg2.pool.ThreadedConnectionPool | None = None
_pool_lock = threading.Lock()

_ENTITY_PREFIXES = {
    "person":       "PERSON",
    "company":      "COMPANY",
    "project_name": "PROJECT",
    "project_code": "PROJCODE",
    "opp_folio":    "OPP",
    "dept":         "DEPT",
    "text_desc":    "DESC",
}

# Fixed advisory lock IDs per entity type
_ADVISORY_LOCK_IDS = {
    "person":       2001,
    "company":      2002,
    "project_name": 2003,
    "project_code": 2004,
    "opp_folio":    2005,
    "dept":         2006,
    "text_desc":    2007,
}

_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS obfuscation_entity_mappings (
    id             SERIAL       PRIMARY KEY,
    entity_type    VARCHAR(50)  NOT NULL,
    original_value TEXT         NOT NULL,
    pseudonym      VARCHAR(100) NOT NULL,
    created_at     TIMESTAMP    DEFAULT NOW(),
    UNIQUE (entity_type, original_value)
);
"""


def _get_pool() -> psycopg2.pool.ThreadedConnectionPool:
    global _pool
    if _pool is None:
        with _pool_lock:
            if _pool is None:
                _pool = psycopg2.pool.ThreadedConnectionPool(
                    minconn=1,
                    maxconn=10,
                    host=settings.db_host,
                    port=settings.db_port,
                    dbname=settings.db_name,
                    user=settings.db_user,
                    password=settings.db_password,
                )
    return _pool


def init_db() -> None:
    pool = _get_pool()
    conn = pool.getconn()
    try:
        with conn.cursor() as cur:
            cur.execute(_CREATE_TABLE)
        conn.commit()
    finally:
        pool.putconn(conn)


def get_all_mappings() -> list[tuple[str, str]]:
    """Returns (pseudonym, original_value) pairs sorted by pseudonym length descending."""
    pool = _get_pool()
    conn = pool.getconn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT pseudonym, original_value FROM obfuscation_entity_mappings "
                "ORDER BY LENGTH(pseudonym) DESC"
            )
            return cur.fetchall()
    finally:
        pool.putconn(conn)


def get_or_create_pseudonym(entity_type: str, original_value: str) -> str:
    prefix = _ENTITY_PREFIXES.get(entity_type, "ENTITY")
    lock_id = _ADVISORY_LOCK_IDS.get(entity_type, 2999)

    pool = _get_pool()
    conn = pool.getconn()
    try:
        with conn.cursor() as cur:
            # Fast path: entity already exists
            cur.execute(
                "SELECT pseudonym FROM obfuscation_entity_mappings "
                "WHERE entity_type = %s AND original_value = %s",
                (entity_type, original_value),
            )
            row = cur.fetchone()
            if row:
                conn.commit()
                return row[0]

            # Slow path: acquire per-entity-type advisory lock to serialize inserts
            cur.execute("SELECT pg_advisory_xact_lock(%s)", (lock_id,))

            # Re-check after acquiring lock (another thread may have inserted)
            cur.execute(
                "SELECT pseudonym FROM obfuscation_entity_mappings "
                "WHERE entity_type = %s AND original_value = %s",
                (entity_type, original_value),
            )
            row = cur.fetchone()
            if row:
                conn.commit()
                return row[0]

            cur.execute(
                "SELECT COUNT(*) FROM obfuscation_entity_mappings WHERE entity_type = %s",
                (entity_type,),
            )
            count = cur.fetchone()[0]
            pseudonym = f"{prefix}_{count + 1:03d}"

            cur.execute(
                "INSERT INTO obfuscation_entity_mappings (entity_type, original_value, pseudonym) "
                "VALUES (%s, %s, %s)",
                (entity_type, original_value, pseudonym),
            )
            conn.commit()
            return pseudonym
    except Exception:
        conn.rollback()
        raise
    finally:
        pool.putconn(conn)
