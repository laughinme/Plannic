import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from core.settings import Settings
from api import api_router
from scheduler import start_scheduler

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    yield

app = FastAPI(
    lifespan=lifespan,
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION,
)

app.include_router(api_router)


@app.get("/ping")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
