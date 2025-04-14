from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class Class(Base):
    __tablename__ = "classes"
    
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    
    schedule: Mapped[list["Schedule"]] = relationship("Schedule", back_populates='_class') # type: ignore


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    
    schedule: Mapped[list["Schedule"]] = relationship("Schedule", back_populates='group') # type: ignore


class ClassRoom(Base):
    __tablename__ = "classrooms"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    
    schedule: Mapped[list["Schedule"]] = relationship("Schedule", back_populates='classroom') # type: ignore
