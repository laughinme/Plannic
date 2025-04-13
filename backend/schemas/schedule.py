from pydantic import BaseModel, Field
from typing import Optional

from models import WeekDay


class Lesson(BaseModel):
    number: int
    subject: Optional[str] = None
    teacher: Optional[str] = None
    room: Optional[str] = None
    group: Optional[str] = None

    start_time: str
    end_time: str
    is_active: bool


class DaySchedule(BaseModel):
    day: WeekDay
    lessons: list[Lesson]


class ClassSchedule(BaseModel):
    class_id: str
    schedule: list[DaySchedule]
    
    
class AllSchedules(BaseModel):
    classes: list[ClassSchedule]
    
    


    

    

