from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

from services.schedule.update import parse_schedule

scheduler = AsyncIOScheduler()

def start_scheduler():
    """
    Schedule will be parsed from school website every 5 minutes
    """
    
    scheduler.add_job(
        func=_run_parse_task,
        trigger='interval',
        seconds=2
    )
    scheduler.start()

def _run_parse_task():
    asyncio.run(parse_schedule())
