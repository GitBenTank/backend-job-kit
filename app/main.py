import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import health, users

logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events."""
    # Startup
    logger.info(
        f"Starting {settings.APP_NAME} | ENV={settings.ENV} | API_PREFIX={settings.API_PREFIX}"
    )
    yield
    # Shutdown (if needed in the future)


app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

# CORS middleware for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite default
        "http://localhost:3000",  # Next.js default
        "http://localhost:8000",  # FastAPI docs
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix=settings.API_PREFIX)
app.include_router(users.router, prefix=settings.API_PREFIX)
