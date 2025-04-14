from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from repositories.schedule_repo import ScheduleRepo
from services.schedule_service import ScheduleService
from db import get_db


def get_schedule_service(session: AsyncSession = Depends(get_db)) -> ScheduleService:
    """Factory function to create a ScheduleService with its dependencies"""
    schedule_repo = ScheduleRepo(session)
    return ScheduleService(schedule_repo)
