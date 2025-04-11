import httpx
import json
from bs4 import BeautifulSoup

from core.settings import Settings

settings = Settings()

async def parse_schedule(path: str = None) -> dict:
    async with httpx.AsyncClient() as client:
        html = await client.get(settings.SCHEDULE_URL)
        html.raise_for_status()
        
        soup = BeautifulSoup(html.text, 'lxml')
        scripts = soup.find_all('script', type='text/javascript')
        parsing_url = next((src.get('src') for src in scripts if str(src.get('src')).startswith('nika_data')), None)
        
        if not parsing_url:
            raise ValueError("Could not find schedule data URL")
            
        schedule_json = await client.get(parsing_url)
        schedule_json.raise_for_status()
        
        content = json.loads(schedule_json.text.split("=", 1)[1].strip().rstrip(";"))
        
        return content
