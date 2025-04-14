from pydantic import BaseModel, Field
from typing import Optional
from datetime import time

from models import WeekDay

class ORMModel(BaseModel):
    pass

    class Config():
        from_attributes = True
    
        

class IdName(ORMModel):
    id: str
    name: str
    
    class Config():
        from_attributes = True
    
class LessonTime(ORMModel):
    start_time: time
    end_time: time
    
    class Config():
        from_attributes = True

class Lesson(ORMModel):
    lesson_number: int
    subject: Optional[IdName] = None
    teacher: Optional[IdName] = None
    classroom: Optional[IdName] = None
    group: Optional[IdName] = None

    lesson_time: LessonTime
    is_active: bool
    
    class Config():
        from_attributes = True


class DaySchedule(ORMModel):
    day: WeekDay
    lessons: list[Lesson]
    
    class Config():
        from_attributes = True


class ClassSchedule(ORMModel):
    class_id: str
    schedule: list[DaySchedule]
