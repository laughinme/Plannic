from typing import AsyncGenerator
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import(
    create_async_engine,
    async_sessionmaker,
    AsyncSession, 
    AsyncEngine
)

from core.settings import Settings

settings = Settings()
engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=True)
async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Returns prepared postgres session"""
    async with async_session() as session:
        yield session

@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Returns prepared postgres session"""
    async with async_session() as session:
        yield session