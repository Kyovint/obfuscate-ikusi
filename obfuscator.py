from datetime import datetime, timedelta
from typing import Any

from column_classifier import ColType, classify_column
from entity_store import get_or_create_pseudonym
from config import settings

_ENTITY_COLUMN_TYPES = {
    ColType.PERSON,
    ColType.COMPANY,
    ColType.PROJECT_NAME,
    ColType.PROJECT_CODE,
    ColType.OPP_FOLIO,
    ColType.DEPT,
    ColType.TEXT_DESC,
}

_DATE_FORMATS = ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d")


def _mask_monetary(value: Any, factor: float) -> Any:
    if value is None:
        return None
    try:
        return round(float(value) * factor, 6)
    except (TypeError, ValueError):
        return value


def _shift_date(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, str):
        for fmt in _DATE_FORMATS:
            try:
                shifted = datetime.strptime(value, fmt) + timedelta(days=settings.date_offset_days)
                return shifted.strftime(fmt)
            except ValueError:
                continue
    return value


def _obfuscate_cell(col_type: ColType, value: Any) -> Any:
    if col_type == ColType.MONETARY_COP:
        return _mask_monetary(value, settings.cop_factor)

    if col_type == ColType.MONETARY_USD:
        return _mask_monetary(value, settings.usd_factor)

    if col_type in _ENTITY_COLUMN_TYPES:
        if value is None or str(value).strip() == "":
            return value
        return get_or_create_pseudonym(col_type.value, str(value).strip())

    if col_type == ColType.DATE:
        return _shift_date(value)

    return value  # PASSTHROUGH


def obfuscate_dataset(columns: list[str], rows: list[list[Any]]) -> list[list[Any]]:
    col_types = [classify_column(col) for col in columns]
    return [
        [_obfuscate_cell(col_types[i], val) for i, val in enumerate(row)]
        for row in rows
    ]
