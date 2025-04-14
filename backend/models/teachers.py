from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base

class Teacher(Base):
    __tablename__ = "teachers"
    
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    
    schedule: Mapped[list["Schedule"]] = relationship("Schedule", back_populates='teacher') # type: ignore
