from sqlalchemy import String, Integer, Time, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import time, date

from db import Base


class Period(Base):
    __tablename__ = "periods"
    
    id: Mapped[str] = mapped_column(String, primary_key=True)
    begin: Mapped[date] = mapped_column(Date, nullable=False)
    end: Mapped[date] = mapped_column(Date, nullable=False)
    

class LessonTimes(Base):
    __tablename__ = "times"
    
    number: Mapped[int] = mapped_column(Integer, primary_key=True)
    start_time: Mapped[time] = mapped_column(Time)
    end_time: Mapped[time] = mapped_column(Time)
    
    schedule: Mapped[list["Schedule"]] = relationship("Schedule", back_populates='lesson_time') # type: ignore
