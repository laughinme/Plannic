import asyncio

from db import get_session
from repositories import DataLoadInterface
from pathlib import Path
from .parsing import parse_schedule
from .exchanges import apply_exchanges
from .update import load_datasets, create_schedule, clear_all
from .utils import generate_hashes

BASE_DIR = Path(__file__).resolve().parent

async def update_schedule_db():
    content = await parse_schedule()
    
    async with get_session() as session:
        async with session.begin():
            dao = DataLoadInterface(session)
            
            old_hashes = await dao.load_hashes()
            new_hashes = generate_hashes(content)
            
            if not old_hashes or (
                old_hashes.schedule != new_hashes.schedule or
                old_hashes.teachers != new_hashes.teachers or
                old_hashes.subjects != new_hashes.subjects or
                old_hashes.classes != new_hashes.classes or
                old_hashes.rooms != new_hashes.rooms or
                old_hashes.classgroups != new_hashes.classgroups or
                old_hashes.periods != new_hashes.periods or
                old_hashes.lesson_times != new_hashes.lesson_times
            ):
                print('REWRITE')
                await clear_all(dao)
                await load_datasets(content, dao)
                await create_schedule(content, dao)
                await apply_exchanges(content, dao)
                await dao.save_hashes(new_hashes)
                
            elif old_hashes.exchanges != new_hashes.exchanges:
                await apply_exchanges(content, dao)
                await dao.save_hashes(new_hashes)


if __name__ == '__main__':
    asyncio.run(update_schedule_db())
