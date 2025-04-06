from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import(
    create_async_engine,
    async_sessionmaker,
    AsyncSession, 
    AsyncEngine
)

from app.core.settings import Settings

settings = Settings()
engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=True)
async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Returns prepared postgres session"""
    async with async_session() as session:
        yield session



