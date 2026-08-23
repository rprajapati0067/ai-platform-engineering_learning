from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Enterprise AI Platform"
    environment: str = "development"
    log_level: str = "INFO"


settings = Settings()
