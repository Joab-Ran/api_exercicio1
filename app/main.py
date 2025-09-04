
from fastapi import FastAPI
from app.core.config import settings
from app.routers import health
from app.routers import me

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

@app.get("/")
def read_root():
    return {"message":"API está funcionando"}

app.include_router(health.router)

app.include_router(me.router) 
