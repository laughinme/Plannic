from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from repositories import ScheduleRepo, UserRepo
from .schedule_service import ScheduleService
from .user_service import UserService
from db import get_db


async def get_schedule_service(session: AsyncSession = Depends(get_db)) -> ScheduleService:
    """Factory function to create a ScheduleService with its dependencies"""
    schedule_repo = ScheduleRepo(session)
    return ScheduleService(schedule_repo)


async def get_user_service(session: AsyncSession = Depends(get_db)) -> UserService:
    """Factory function to create a UserService with its dependencies"""
    user_repo = UserRepo(session)
    return UserService(user_repo)
