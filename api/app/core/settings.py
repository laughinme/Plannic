from typing import List
from pydantic_settings import BaseSettings
# from pydantic import AnyHttpUrl

class Settings(BaseSettings):
    # API settings
    API_PREFIX: str = "/api"
    PROJECT_NAME: str = "Plannic API"
    PROJECT_DESCRIPTION: str = "FastAPI backend for Plannic application"
    VERSION: str = "0.1.0"
    
    # Security and CORS
    SECRET_KEY: str = "your-secret-key-here"  # Change this in production!
    # CORS_ORIGINS: List[AnyHttpUrl] = []
    
    # Database settings
    DATABASE_URL: str = ""
    
    # Bot notification settings
    BOT_WEBHOOK_URL: str = "http://bot:8000/webhook"
    
    class Config:
        env_file = ".env"
        case_sensitive = True 