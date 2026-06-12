from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "ikusito_db"
    db_user: str = "ikusiAdm"
    db_password: str = ""
    cop_factor: float = 0.000001
    usd_factor: float = 0.001
    date_offset_days: int = -365


settings = Settings()
