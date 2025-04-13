from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from models import Schedule, WeekDay

class ScheduleRepo:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    
    async def get_day_lessons(self, class_id: str, day: WeekDay):
        print(day.name)
        query = (
            select(Schedule)
            .options(
                selectinload(Schedule.subject),
                selectinload(Schedule.teacher),
                selectinload(Schedule.classroom),
                selectinload(Schedule.group),
                selectinload(Schedule.lesson_time),
            )
            .where(
                Schedule.day == day.name,
                Schedule.class_id == class_id,
            )
        )
        day_schedule = await self.session.scalars(query)
        day_schedule = day_schedule.all()
        print(day_schedule)
        return day_schedule
        
        