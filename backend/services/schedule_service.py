

from repositories import ScheduleRepo
from models import WeekDay

class ScheduleService():
    def __init__(self, schedule_repo: ScheduleRepo):
        self.schedule_repo = schedule_repo
        
    async def get_schedule(
        self, 
        class_id: str,
        day: WeekDay
        
    ):
        return await self.schedule_repo.get_day_lessons(class_id, day)