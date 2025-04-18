from redis.asyncio import Redis
from core.settings import Settings
from typing import AsyncGenerator

settings = Settings()

redis_client = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT
)

async def get_redis() -> AsyncGenerator[Redis, None]:
    "Returns prepared Redis session"
    yield redis_client