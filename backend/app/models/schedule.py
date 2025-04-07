from sqlalchemy import ForeignKey, Integer, String, Enum, Time, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import time

from .classes import ClassRoom, Group, Class
from .lessons import Lesson
from .enums import WeekDay
from .teachers import Teacher

from app.db import Base

class Period(Base):
    __tablename__ = "periods"
    
    prefix: Mapped[str] = mapped_column(String, primary_key=True)
    period: Mapped[str] = mapped_column(String, nullable=False)
    
    
class Schedule(Base):
    __tablename__ = "schedule"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    class_id: Mapped[str] = mapped_column(String, ForeignKey("classes.id"))
    day: Mapped[WeekDay] = mapped_column(Enum(WeekDay), nullable=False)
    
    lesson_number: Mapped[int] = mapped_column(Integer, nullable=False)
    lesson_id: Mapped[str] = mapped_column(String, ForeignKey("lessons.id"))
    teacher_id: Mapped[str] = mapped_column(String, ForeignKey("teachers.id"))
    classroom_id: Mapped[str] = mapped_column(String, ForeignKey("classrooms.id"))
    group_id: Mapped[str] = mapped_column(String, ForeignKey('groups.id'), nullable=True)
    
    start_time: Mapped[time] = mapped_column(Time)
    end_time: Mapped[time] = mapped_column(Time)
    
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    
    
    _class: Mapped[Class] = relationship(Class, back_populates="schedule")
    lesson: Mapped[Lesson] = relationship(Lesson, back_populates="schedule")
    teacher: Mapped[Teacher] = relationship(Teacher, back_populates="schedule")
    classroom: Mapped[ClassRoom] = relationship(ClassRoom, back_populates="schedule")
    group: Mapped[Group] = relationship(Group, back_populates="schedule")
