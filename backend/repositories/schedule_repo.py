from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from models import Schedule, WeekDay

class ScheduleRepo:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    def basic_selection(self):
        query = (
            select(Schedule)
            .options(
                selectinload(Schedule.subject),
                selectinload(Schedule.teacher),
                selectinload(Schedule.classroom),
                selectinload(Schedule.group),
                selectinload(Schedule.lesson_time),
            )
        )
        return query
    
    async def get_day_lessons(self, class_id: str, day: WeekDay) -> list[Schedule]:
        query = (
            self.basic_selection()
            .where(
                Schedule.day == day.name,
                Schedule.class_id == class_id,
            )
            .order_by(Schedule.lesson_number)
        )
        result = await self.session.scalars(query)
        day_schedule = result.all()
        return day_schedule


    async def get_week_lessons(self, class_id: str) -> list[Schedule]:
        query = (
            self.basic_selection()
            .where(Schedule.class_id == class_id)
            .order_by(Schedule.day)
        )
        result = await self.session.scalars(query)
        week_schedule = result.all()
        return week_schedule
    
    
    async def get_all_lessons(self) -> list[Schedule]:
        query = (
            self.basic_selection()
            .order_by(Schedule.class_id, Schedule.day)
        )
        result = await self.session.scalars(query)
        all_schedules = result.all()
        return all_schedules