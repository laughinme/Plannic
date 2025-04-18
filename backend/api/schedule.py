from fastapi import APIRouter, Depends, Query

from schemas import (
    Lesson,
    DaySchedule,
    ClassSchedule,
)
from services import ScheduleService, get_schedule_service
from models import WeekDay
from db import get_session

router = APIRouter(prefix='/schedule', tags=['Schedule'])


@router.get(
    '/all',
    response_model=list[ClassSchedule],
)
async def all_schedules(
    schedule_service: ScheduleService = Depends(get_schedule_service)
):
    schedule = await schedule_service.get_all_schedules()
    return schedule


@router.get(
    '/class',
    response_model=list[DaySchedule],
)
async def class_schedules(
    class_id: str = Query(..., description="Id of the class to get the schedule for"),
    schedule_service: ScheduleService = Depends(get_schedule_service)
):
    schedule = await schedule_service.get_week_schedule(class_id)
    return schedule


@router.get(
    '/day',
    response_model=list[Lesson],
)
async def day_schedules(
    class_id: str = Query(..., description="Id of the class to get the schedule for"),
    day: WeekDay = Query(..., description="Day to get the schedule for"),
    schedule_service: ScheduleService = Depends(get_schedule_service)
):
    schedule = await schedule_service.get_day_schedule(class_id, day)
    return schedule
