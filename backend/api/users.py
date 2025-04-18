from fastapi import APIRouter, Depends, Query
from uuid import UUID

from schemas import UserOut, UserPatch
from services import UserService, get_user_service
from core.security import verify_api_key

router = APIRouter(prefix="/users", tags=['Users'])

@router.patch(
    "/edit",
    response_model=UserOut,
    status_code=201
)
async def edit_user(
    payload: UserPatch,
    user_id: UUID = Query(...),
    user_service: UserService = Depends(get_user_service),
    api_key: str = Depends(verify_api_key)
):
    user = await user_service.edit_user(payload, user_id)
    return user
