import uvicorn
from fastapi import FastAPI

from core.settings import Settings
from api import api_router

settings = Settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION,
)

app.include_router(api_router, prefix=settings.API_PREFIX)


@app.get("/ping")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
