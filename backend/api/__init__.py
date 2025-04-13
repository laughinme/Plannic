from fastapi import APIRouter

from . import schedule

api_router = APIRouter(prefix='/api')

api_router.include_router(
    schedule.router, 
    prefix="/schedule", 
    tags=["Schedule"]
)
