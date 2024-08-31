from fastapi import APIRouter

from app.api.routes import pokedex


api_router = APIRouter()

api_router.include_router(pokedex.router, prefix="/pokedex", tags=["pokedex"])
