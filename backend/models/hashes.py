from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped

from db import Base


class Hash(Base):
    __tablename__ = "hashes"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, default=1)
    
    schedule: Mapped[str] = mapped_column(String, nullable=True)
    exchanges: Mapped[str] = mapped_column(String, nullable=True)
    teachers: Mapped[str] = mapped_column(String, nullable=True)
    subjects: Mapped[str] = mapped_column(String, nullable=True)
    classes: Mapped[str] = mapped_column(String, nullable=True)
    rooms: Mapped[str] = mapped_column(String, nullable=True)
    classgroups: Mapped[str] = mapped_column(String, nullable=True)
    periods: Mapped[str] = mapped_column(String, nullable=True)
    lesson_times: Mapped[str] = mapped_column(String, nullable=True)
