from apscheduler.schedulers.asyncio import AsyncIOScheduler

from services.schedule.update import update_schedule_db

scheduler = AsyncIOScheduler()

def start_scheduler():
    """
    Schedule will be parsed from school website every 5 minutes
    """
    
    scheduler.add_job(
        func=update_schedule_db,
        trigger='interval',
        seconds=5
    )
    scheduler.start()
