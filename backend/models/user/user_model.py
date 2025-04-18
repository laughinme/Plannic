from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, Uuid, Boolean
from uuid import UUID, uuid4

from db import Base

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    class_id: Mapped[str] = mapped_column(String, ForeignKey('classes.id'), nullable=True, default="000")
    group_id: Mapped[str] = mapped_column(String, ForeignKey('groups.id'), nullable=True, default="3")
    
    notify_day_end: Mapped[bool] = mapped_column(Boolean, default=False)
    notify_before_lesson: Mapped[bool] = mapped_column(Boolean, default=True)
    notify_exchanges: Mapped[bool] = mapped_column(Boolean, default=True)
