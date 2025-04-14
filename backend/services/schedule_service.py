
from schemas import *
from repositories import ScheduleRepo
from models import WeekDay, Schedule

class ScheduleService():
    def __init__(self, schedule_repo: ScheduleRepo):
        self.schedule_repo = schedule_repo

    async def get_day_schedule(
        self, 
        class_id: str,
        day: WeekDay
    ) -> list[Schedule]:
        day_data = await self.schedule_repo.get_day_lessons(class_id, day)
        return day_data
    
    async def get_week_schedule(self, class_id: str):
        week_data = await self.schedule_repo.get_week_lessons(class_id)

        grouped_map: dict[str, list] = {}
        for lesson in week_data:
            day = lesson.day
            if day not in grouped_map:
                grouped_map[day] = []
            grouped_map[day].append(lesson)
        
        week_schedules = []
        for day, schedules in grouped_map.items():
            week_schedules.append(
                DaySchedule(
                    day=day,
                    lessons=schedules
                )
            )
            
        return week_schedules
    
    
    async def get_all_schedules(self):
        all_schedules = await self.schedule_repo.get_all_lessons()
        
        grouped_map: dict[str, dict[str, list]] = {}
        for lesson in all_schedules:
            class_id = lesson.class_id
            day = lesson.day
            if class_id not in grouped_map:
                grouped_map[class_id] = {day: []}
                
            if day not in grouped_map[class_id]:
                grouped_map[class_id][day] = []
            
            grouped_map[class_id][day].append(lesson)
            
        all_schedules_out = []
        for class_id, day_schedules in grouped_map.items():
            
            week_schedules = []
            for day, schedules in day_schedules.items():
                week_schedules.append(
                    DaySchedule(
                        day=day,
                        lessons=schedules
                    )
                )
                
            all_schedules_out.append(
                ClassSchedule(
                    class_id=class_id,
                    schedule=week_schedules
                )
            )
            
        return all_schedules_out
        