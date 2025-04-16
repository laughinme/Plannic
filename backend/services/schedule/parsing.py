import httpx
import json
from bs4 import BeautifulSoup

from core.settings import Settings

settings = Settings()

async def parse_schedule(path: str = None) -> dict:
    async with httpx.AsyncClient() as client:
        html = await client.get(settings.MOBILE_SCHEDULE_URL)
        html.raise_for_status()
        
        soup = BeautifulSoup(html.text, 'lxml')
        scripts = soup.find_all('script', type='text/javascript')
        schedule_id = next((src.get('src') for src in scripts if str(src.get('src')).startswith('nika_data')), None)
        
        if not schedule_id:
            raise ValueError("Could not find schedule data URL")
        
        json_url = settings.MOBILE_SCHEDULE_URL.rsplit('/', 1)[0] + '/' + schedule_id
        print(json_url)
        schedule_json = await client.get(json_url)
        schedule_json.raise_for_status()
        
        content = json.loads(schedule_json.text.split("=", 1)[1].strip().rstrip(";"))
        
        return content
