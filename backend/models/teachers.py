from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from db import Base

class Teacher(Base):
    __tablename__ = "teachers"
    
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
