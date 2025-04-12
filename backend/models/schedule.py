from sqlalchemy import ForeignKey, Integer, String, Enum, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .classes import ClassRoom, Group, Class
from .subjects import Subject
from .enums import WeekDay
from .teachers import Teacher

from db import Base
    
    
class Schedule(Base):
    __tablename__ = "schedule"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    class_id: Mapped[str] = mapped_column(String, ForeignKey("classes.id"))
    day: Mapped[WeekDay] = mapped_column(Enum(WeekDay), nullable=False)
    
    lesson_number: Mapped[int] = mapped_column(Integer, nullable=False)
    subject_id: Mapped[str] = mapped_column(String, ForeignKey("subjects.id"))
    teacher_id: Mapped[str] = mapped_column(String, ForeignKey("teachers.id"))
    classroom_id: Mapped[str] = mapped_column(String, ForeignKey("classrooms.id"))
    group_id: Mapped[str] = mapped_column(String, ForeignKey('groups.id'))
    
    lesson_time_id: Mapped[int] = mapped_column(Integer, ForeignKey('times.number'))
    
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    
    
    _class: Mapped[Class] = relationship(Class, back_populates="schedule")
    subject: Mapped[Subject] = relationship(Subject, back_populates="schedule")
    teacher: Mapped[Teacher] = relationship(Teacher, back_populates="schedule")
    classroom: Mapped[ClassRoom] = relationship(ClassRoom, back_populates="schedule")
    group: Mapped[Group] = relationship(Group, back_populates="schedule")
