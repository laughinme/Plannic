import asyncio
from sqlalchemy import delete, text
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type, TypeVar
from datetime import datetime

from .parsing import parse_schedule
from models import (
    WeekDay, 
    Class, 
    Teacher, 
    Subject, 
    ClassRoom, 
    Group,
    LessonTimes,
    Period,
    Schedule
)
from db.session import get_session

T = TypeVar('T')

async def insert_id_name(
    object: dict[str, str],
    model: Type[T],
    session: AsyncSession
) -> None:
    for id, name in object.items():
        query = (
            insert(model)
            .values(id=id, name=name)
            .on_conflict_do_nothing()
        )
        await session.execute(query)
        
        
async def load_dbs(content: dict, session: AsyncSession):
    async with session.begin():
        # Teachers
        teachers: dict[str, str] = content["TEACHERS"]
        await insert_id_name(teachers, Teacher, session)
        
        # Subjects
        subjects: dict[str, str] = content["SUBJECTS"]
        await insert_id_name(subjects, Subject, session)
        
        # Classes
        classes: dict[str, str] = content["CLASSES"]
        await insert_id_name(classes, Class, session)
        
        # Rooms
        rooms: dict[str, str] = content["ROOMS"]
        await insert_id_name(rooms, ClassRoom, session)
        
        # Class groups
        groups: dict[str, str] = content["CLASSGROUPS"]
        await insert_id_name(groups, Group, session)
        
        # Lesson times
        times: dict[str, list[str]] = content["LESSON_TIMES"]
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
            await session.execute(query)
        
        # Periods
        period_index = next(iter(content["PERIODS"]))
        period: dict[str, dict[str, str]] = content["PERIODS"][period_index]
        for point, date in period.items():
            if point == 'b':
                begin = date 
            elif point == 'e':
                end = date
                
        query = (
            insert(Period)
            .values(
                id=period_index,
                begin=begin,
                end=end
            )
            .on_conflict_do_nothing()
        )
        await session.execute(query)
            
        
async def create_schedule(
    content: dict,
    session: AsyncSession
) -> None:
    period = next(iter(content["CLASS_SCHEDULE"]))
    schedule: dict[
        str, dict[str, dict[str, list[str]]]
    ] = content["CLASS_SCHEDULE"][period]
    
    async with session.begin():
        for class_id, records in schedule.items():
            for day_and_lesson_num, lesson in records.items():
                day = WeekDay(day_and_lesson_num[0])
                lesson_number = int(day_and_lesson_num[1:])
                
                for i, subject_id in enumerate(lesson["s"]):
                    teacher_id = lesson["t"][i]
                    classroom_id = lesson["r"][i]
                    
                    group_id = None
                    if "g" in lesson:
                        group_id = lesson["g"][i]
                
                    query = (
                        insert(Schedule)
                        .values(
                            class_id = class_id,
                            day = day,
                            lesson_number = lesson_number,
                            subject_id = subject_id or None,
                            teacher_id = teacher_id or None,
                            classroom_id = classroom_id or None,
                            group_id = group_id or None,
                            lesson_time_id = lesson_number,
                        )
                        .on_conflict_do_nothing()
                    )
                    await session.execute(query)

async def clear_all(session: AsyncSession):
    models = [
        Schedule,
        Class, 
        Teacher, 
        Subject, 
        ClassRoom, 
        Group,
        LessonTimes,
        Period,
    ]
    
    table_names = ", ".join(model.__tablename__ for model in models)
    query = text(f"TRUNCATE TABLE {table_names} RESTART IDENTITY CASCADE")
    
    async with session.begin():
        await session.execute(query)
        


async def update_schedule_db():
    print('starting')
    content = await parse_schedule()
    
    async with get_session() as session:
        await clear_all(session)
        await load_dbs(content, session)
        await create_schedule(content, session)


if __name__ == '__main__':
    asyncio.run(update_schedule_db())
