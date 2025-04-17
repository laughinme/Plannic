from sqlalchemy import select, text, delete, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar, Type
from datetime import datetime, date

from models import LessonTimes, Period, Schedule, WeekDay, Hash
from db import Base

class DataLoadInterface:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    T = TypeVar('T', bound=Base)
        
    async def insert_id_name(
        self,
        object: dict[str, str],
        model: Type[T],
    ) -> None:
        for id, name in object.items():
            query = (
                insert(model)
                .values(id=id, name=name)
                .on_conflict_do_nothing()
            )
            await self.session.execute(query)
                
                
    async def insert_lesson_times(self, times: dict[str, list[str]]):
        for id, time_list in times.items():
            query = (
                insert(LessonTimes)
                .values(
                    number=int(id), 
                    start_time=datetime.strptime(time_list[0], "%H:%M"), 
                    end_time=datetime.strptime(time_list[1], "%H:%M"),
                )
                .on_conflict_do_nothing()
            )
            await self.session.execute(query)
                
                
    async def insert_period(self, period_index: str, begin: date, end: date):
        query = (
            insert(Period)
            .values(
                id=period_index,
                begin=begin,
                end=end
            )
            .on_conflict_do_nothing()
        )
        await self.session.execute(query)


    async def truncate_table(self, model: Type[T]):
        query = text(f"TRUNCATE TABLE {model.__tablename__} RESTART IDENTITY CASCADE")
        
        await self.session.execute(query)
            
            
    async def get_period(self) -> Period:
        period = await self.session.scalar(select(Period))
        return period
    
    
    async def get_same_lesson(
        self,
        day: WeekDay,
        class_id: str,
        subject_id: str,
        teacher_id: str,
        classroom_id: str,
        group_id: str,
    ) -> Schedule:
        query = (
            select(Schedule)
            .where(
                Schedule.day == day,
                Schedule.class_id == class_id,
                Schedule.subject_id == subject_id,
                Schedule.teacher_id == teacher_id,
                Schedule.classroom_id == classroom_id,
                Schedule.group_id == group_id,
            )
        )
        lesson = await self.session.scalar(query)
        return lesson
    
    
    async def get_lessons_by_number(
        self,
        class_id: str,
        day: WeekDay,
        lesson_number: int
    ) -> list[Schedule]:

        query = (
            select(Schedule)
            .where(
                Schedule.class_id == class_id,
                Schedule.day == day,
                Schedule.lesson_number == lesson_number,
            )
            .order_by(Schedule.group_id)
        )
        
        result = await self.session.scalars(query)
        lessons: list[Schedule] = result.all()
        # return sorted(lessons, key=lambda x: int(x.group_id or 0))
        return lessons
        

    async def cancel_lesson(
        self,
        class_id: str,
        day: WeekDay,
        lesson_number: int,
    ) -> None:
        query = (
            update(Schedule)
            .where(
                Schedule.class_id == class_id,
                Schedule.day == day,
                Schedule.lesson_number == lesson_number,
            )
            .values(is_active=False)
        )
        await self.session.execute(query)
            
    
    async def insert_lesson(self, lesson: Schedule):
        self.session.add(lesson)


    async def delete_lesson(
        self,
        class_id: str,
        day: WeekDay,
        lesson_number: int
    ) -> None:
        query = (
            delete(Schedule)
            .where(
                Schedule.class_id == class_id,
                Schedule.day == day,
                Schedule.lesson_number == lesson_number,
            )
        )
        await self.session.execute(query)
            
    
    async def update_lesson(
        self,
        lesson: Schedule
    ) -> None:
        basic_query = (
            update(Schedule)
            .where(
                Schedule.class_id == lesson.class_id,
                Schedule.day == lesson.day,
                Schedule.lesson_number == lesson.lesson_number,
                Schedule.group_id == lesson.group_id
            )
        )
        if lesson.is_active == False:
            query = basic_query.values(is_active=False)
            await self.session.execute(query)
            return
            
            
        query = basic_query.values(
            subject_id=lesson.subject_id,
            teacher_id=lesson.teacher_id,
            group_id=lesson.group_id,
            classroom_id=lesson.classroom_id,
        )
        
        await self.session.execute(query)


    async def load_hashes(self) -> Hash:
        hashes = await self.session.scalar(
            select(Hash).limit(1)
        )
        return hashes
    
    async def save_hashes(self, hashes: Hash) -> None:
        row = await self.load_hashes()
        if not row:
            self.session.add(hashes)
            return
        
        await self.session.execute(delete(Hash))
        self.session.add(hashes)
    
