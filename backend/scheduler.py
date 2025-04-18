from apscheduler.schedulers.asyncio import AsyncIOScheduler

from services.schedule import update_schedule_db

scheduler = AsyncIOScheduler()

def start_scheduler():
    """
    Schedule will be parsed from school website every 5 minutes
    """
    
    scheduler.add_job(
        func=update_schedule_db,
        trigger='interval',
        seconds=60
    )
    scheduler.start()
