from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from .settings import Settings

settings = Settings()

api_key_header = APIKeyHeader(name=settings.HEADER_NAME, auto_error=False)

async def verify_api_key(api_key = Security(api_key_header)):
    if not api_key or api_key != settings.SECRET_KEY:
        raise HTTPException(
            status_code=403, 
            detail="Service API key is incorrect"
        )
        
    return api_key
