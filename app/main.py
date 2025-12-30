from fastapi import FastAPI
from app.routers import health, users

app = FastAPI(title="Backend Job Kit API")

app.include_router(health.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")

