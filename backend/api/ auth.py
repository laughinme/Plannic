from fastapi import APIRouter, Depends

from schemas import UserSchema, UserOut
from services import UserService, get_user_service
from core.security import verify_api_key

router = APIRouter(prefix="/auth", tags=['Auth'])

@router.post(
    "/register",
    response_model=UserOut,
    status_code=201
)
async def register_user(
    payload: UserSchema,
    user_service: UserService = Depends(get_user_service),
    api_key: str = Depends(verify_api_key)
):
    user = await user_service.register_user(payload)
    return user


# @router.post(
#     "/service",
# )
# async def auth_service(
#     api_key: str = Depends(verify_api_key)
# ):
#     pass
