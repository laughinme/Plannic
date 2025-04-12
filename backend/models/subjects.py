from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from db import Base

class Subject(Base):
    """School subject model. Name field contains subject name with emoji."""
    
    __tablename__ = "subjects"
    
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


class SubjectEmoji(Base):
    """Subject emoji model."""
    
    __tablename__ = "subject_emojis"
    
    name: Mapped[str] = mapped_column(String, primary_key=True)
    emoji: Mapped[str] = mapped_column(String, nullable=False)

