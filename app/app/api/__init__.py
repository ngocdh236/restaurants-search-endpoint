from fastapi import APIRouter

from app.api import restaurants

api_router = APIRouter()

api_router.include_router(
    restaurants.router, prefix="/restaurants", tags=["restaurants"])
