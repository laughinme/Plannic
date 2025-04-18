from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from models import User
from schemas import UserSchema, UserPatch

class UserRepo:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    
    async def save_user(self, payload: UserSchema) -> User:
        query = (
            insert(User)
            .values(**payload.model_dump())
            .on_conflict_do_nothing()
            .returning(User)
        )
        result = await self.session.execute(query)
        user = result.scalar()
        return user


    async def edit_user(
        self, 
        payload: dict,
        user_id: UUID
    ) -> User:
        query = (
            update(User)
            .values(**payload)
            .where(User.id == user_id)
            .returning(User)
        )
        result = await self.session.execute(query)
        user = result.scalar()
        return user
    
    
        