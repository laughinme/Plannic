import asyncio
from sqlalchemy import select

from .parsing import parse_schedule
from models import WeekDay


async def update_schedule_db():
    content = await parse_schedule()
    print(content)
    
    for day in WeekDay:
        print(day)
    
    



if __name__ == '__main__':
    asyncio.run(update_schedule_db())
