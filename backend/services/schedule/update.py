import asyncio
from datetime import datetime

from .parsing import parse_schedule
from .exchanges import apply_exchanges
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
from repositories import DataLoadInterface
from .utils import setup_lessons
        
        
async def load_datasets(
    content: dict,
    dao: DataLoadInterface
) -> None:
    # Teachers
    teachers: dict[str, str] = content["TEACHERS"]
    await dao.insert_id_name(teachers, Teacher)
    
    # Subjects
    subjects: dict[str, str] = content["SUBJECTS"]
    await dao.insert_id_name(subjects, Subject)
    
    # Classes
    classes: dict[str, str] = content["CLASSES"]
    await dao.insert_id_name(classes, Class)
    
    # Rooms
    rooms: dict[str, str] = content["ROOMS"]
    await dao.insert_id_name(rooms, ClassRoom)
    
    # Class groups
    groups: dict[str, str] = content["CLASSGROUPS"]
    await dao.insert_id_name(groups, Group)
    
    # Lesson times
    times: dict[str, list[str]] = content["LESSON_TIMES"]
    await dao.insert_lesson_times(times)
    
    # Period
    period_index = next(iter(content["PERIODS"]))
    period: dict[str, dict[str, str]] = content["PERIODS"][period_index]
    for point, date in period.items():
        if point == 'b':
            begin = datetime.strptime(date, '%d.%m.%Y').date()
        elif point == 'e':
            end = datetime.strptime(date, '%d.%m.%Y').date()
        
    await dao.insert_period(period_index, begin, end)
            
        
async def create_schedule(
    content: dict,
    dao: DataLoadInterface
) -> None:
    period = next(iter(content["CLASS_SCHEDULE"]))
    schedule: dict[
        str, dict[str, dict[str, list[str]]]
    ] = content["CLASS_SCHEDULE"][period]
    
    for class_id, records in schedule.items():
        print(class_id)
        for day_and_lesson_num, lesson in records.items():
                        
            new_lessons = setup_lessons(
                class_id=class_id,
                lesson_number=int(day_and_lesson_num[1:]),
                day=WeekDay(day_and_lesson_num[0]),
                lesson=lesson,
            )
            
            for new_lesson in new_lessons:
                print(new_lesson)
                if not new_lesson.subject_id:
                    continue
                
                await dao.insert_lesson(new_lesson)
                

async def clear_all(dao: DataLoadInterface):
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
    
    for model in models:
        await dao.truncate_table(model)
        


async def update_schedule_db():
    print('starting')
    content = await parse_schedule()
    
    async with get_session() as session:
        async with session.begin():
            dao = DataLoadInterface(session)
            
            await clear_all(dao)
            await load_datasets(content, dao)
            await create_schedule(content, dao)
            await apply_exchanges(content, dao)


if __name__ == '__main__':
    asyncio.run(update_schedule_db())
