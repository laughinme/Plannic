from uuid import UUID

from schemas import UserSchema, UserPatch
from repositories import UserRepo
from models import User

class UserService():
    def __init__(self, schedule_repo: UserRepo):
        self.schedule_repo = schedule_repo

    async def register_user(
        self, 
        payload: UserSchema
    ) -> User:
        user = await self.schedule_repo.save_user(payload)
        return user
    
    async def edit_user(
        self, 
        payload: UserPatch,
        user_id: UUID
    ) -> User:
        edited_fields = payload.model_dump(exclude_none=True)
        user = await self.schedule_repo.edit_user(edited_fields, user_id)
        return user
        
    