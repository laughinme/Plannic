from pydantic import Field
from uuid import UUID, uuid4
from typing import Optional

from .orm import ORMModel


class UserSchema(ORMModel):
    id: Optional[UUID] = Field(uuid4)
    telegram_id: Optional[UUID] = Field(None)
    name: str
    

class UserOut(ORMModel):
    id: UUID
    telegram_id: UUID
    name: str
    class_id: str
    group_id: str
    
    notify_day_end: bool
    notify_before_lesson: bool
    notify_exchanges: bool
    
    
class UserPatch(ORMModel):
    class_id: Optional[str] = Field(None, max_length=3)
    group_id: Optional[str] = Field(None, max_length=1)
    notify_day_end: Optional[bool] = Field(None)
    notify_before_lesson: Optional[bool] = Field(None)
    notify_exchanges: Optional[bool] = Field(None)
    

# class UserRegister(ORMModel):
#     id: Optional[UUID] = Field(uuid4)
#     telegram_id: Optional[UUID] = Field(None)
#     name: str
#     class_id: str = Field(max_length=3)
#     group_id: str = Field(max_length=1)


# class UserOut(ORMModel):
#     id: UUID
#     telegram_id: Optional[UUID] = None
#     name: str
#     class_id: str
#     group_id: str
