from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    # API settings
    API_PREFIX: str = "/api"
    PROJECT_NAME: str = "Plannic API"
    PROJECT_DESCRIPTION: str = "FastAPI backend for Plannic application"
    VERSION: str = "0.1.0"
    
    # API authorization
    HEADER_NAME: str = "X-API-Key"
    SECRET_KEY: str

    # Bot notification settings
    BOT_WEBHOOK_URL: str = "http://bot:8000/webhook"
    
    # Basic config
    MOBILE_SCHEDULE_URL: str = "https://lyceum.nstu.ru/rasp/m.schedule.html"
    
    # Redis settings
    REDIS_HOST: str = "redis"
    REDIS_PORT: str = "6379"
    
    # Database settings
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    
    @property
    def DB_URL(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )
    
    class Config:
        env_file = f"{BASE_DIR}/.env"
        # case_sensitive = True 
        extra = "allow"
        