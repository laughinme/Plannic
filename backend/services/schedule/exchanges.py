import asyncio
from datetime import date as dtmDate, timedelta, datetime

from models import WeekDay, Period
from repositories import DataLoadInterface
from .utils import setup_lessons, lessons_equal


async def get_day_number(date: dtmDate, period: Period) -> WeekDay:
    date = datetime.strptime(date, '%d.%m.%Y').date()
    difference = date - period.begin
    day = WeekDay(str(difference.days))
    
    return day
    

async def apply_exchanges(
    content: dict,
    dao: DataLoadInterface
) -> None:
    class_exchange: dict[
        str, dict[str, dict[str, dict[str, list[str]]]]
    ] = content["CLASS_EXCHANGE"]
    period = await dao.get_period()
    print('APPLY EXCHANGES')
    
    for class_id, changes in class_exchange.items():
        for date, lessons in changes.items():
            day = await get_day_number(date, period)
            for lesson_number, lesson in lessons.items():
                lesson_number = int(lesson_number)
                
                if lesson["s"] == "F":
                    await dao.cancel_lesson(class_id, day, lesson_number)
                    continue
                
                exchanges = setup_lessons(
                    class_id, lesson_number, day, lesson
                )
                
                existing_lessons = await dao.get_lessons_by_number(class_id, day, lesson_number)
                
                # Add new lessons
                if len(existing_lessons) == 0:
                    for new_lesson in exchanges:
                            await dao.insert_lesson(new_lesson)
                
                # If there was division by groups
                elif len(existing_lessons) > 1:
                    # If lesson exchanges are also divided by groups
                    if len(exchanges) > 1:
                        for index in range(len(exchanges)):
                            existing_lesson = existing_lessons[index]
                            new_lesson = exchanges[index]
                            
                            if lessons_equal(existing_lesson, new_lesson):
                                continue
                            
                            await dao.update_lesson(new_lesson)
                            
                    # If there were 2 lessons for groups, and now only 1
                    else:
                        await dao.delete_lesson(class_id, day, lesson_number)
                        await dao.insert_lesson(exchanges[0])
                        
                else:
                    # Case when there was only 1 lesson, and now there are 2
                    if len(exchanges) > 1:
                        await dao.delete_lesson(class_id, day, lesson_number)
                        
                        for new_lesson in exchanges:
                            await dao.insert_lesson(new_lesson)
                    
                    # One lesson replaced with another one
                    else:
                        new_lesson = exchanges[0]
                        if lessons_equal(existing_lessons[0], new_lesson):
                            continue
                        
                        await dao.update_lesson(new_lesson)
                    
    
if __name__ == "__main__":
    pass
