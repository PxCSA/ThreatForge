from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "ThreatForge API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file="backend/.env",
        extra="ignore",
    )


settings = Settings()