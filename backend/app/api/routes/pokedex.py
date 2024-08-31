from typing import List
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from app.api.crud import pokedex as crud_pokedex
from app.api.schemas.pokedex import (
    PokedexBase,
    PokedexCreate,
    PokedexUpdate,
    PokedexOut,
)

router = APIRouter()


@router.get("/{pokemon_identifier}", response_model=PokedexBase)
def get_pokemon(pokemon_identifier: str):
    try:
        answer = crud_pokedex.get_pokemon(pokemon_identifier=pokemon_identifier)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to get data: {e}")

    return answer
