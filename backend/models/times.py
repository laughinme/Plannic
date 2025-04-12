from sqlalchemy import String, Integer, Time
from sqlalchemy.orm import Mapped, mapped_column
from datetime import time

from db import Base


class Period(Base):
    __tablename__ = "periods"
    
    prefix: Mapped[str] = mapped_column(String, primary_key=True)
    period: Mapped[str] = mapped_column(String, nullable=False)
    

class LessonTimes(Base):
    __tablename__ = "times"
    
    number: Mapped[int] = mapped_column(Integer, primary_key=True)
    start_time: Mapped[time] = mapped_column(Time)
    end_time: Mapped[time] = mapped_column(Time)
