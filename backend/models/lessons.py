from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from db import Base

class Lesson(Base):
    """School lesson model. Name field contains lesson name with emoji."""
    
    __tablename__ = "lessons"
    
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


class LessonEmoji(Base):
    """Lesson emoji model."""
    
    __tablename__ = "lesson_emojis"
    
    name: Mapped[str] = mapped_column(String, primary_key=True)
    emoji: Mapped[str] = mapped_column(String, nullable=False)

