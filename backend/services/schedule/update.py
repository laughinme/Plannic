import asyncio
from sqlalchemy import select

from .parsing import parse_schedule
from models import WeekDay


async def update_schedule_db():
    print('starting')
    content = await parse_schedule()

    
    for day in WeekDay:
        pass
    
    


if __name__ == '__main__':
    asyncio.run(update_schedule_db())
