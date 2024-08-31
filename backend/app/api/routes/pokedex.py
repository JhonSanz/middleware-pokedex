from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from app.api.crud import pokedex as crud_pokedex
from app.api.schemas.pokedex import PokedexBase, PokedexAll


router = APIRouter()


@router.get("/{pokemon_identifier}", response_model=PokedexBase)
def get_pokemon(pokemon_identifier: str):
    """
    Endpoint para obtener la información de un Pokémon específico por su identificador.

    params:
    - pokemon_identifier (str): Identificador único del Pokémon, puede ser el nombre o el ID en la Pokédex.

    returns:
    - PokedexBase: Objeto que contiene la información básica del Pokémon.
    """
    try:
        answer = crud_pokedex.get_pokemon(pokemon_identifier=pokemon_identifier)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to get data: {e}")

    return answer


@router.get("/", response_model=List[PokedexAll])
def get_pokemons(
    skip: int = Query(
        0, description="Número de registros a omitir desde el inicio de la lista"
    ),
    limit: int = Query(10, description="Número máximo de registros a devolver"),
):
    """
    Endpoint para obtener una lista paginada de Pokémon.

    params:
    - skip (int): Número de registros a omitir desde el inicio de la lista.
    - limit (int): Número máximo de registros a devolver.

    returns:
    - PokedexAll: Objeto que contiene la lista de Pokémon y la cantidad total.
    """
    try:
        answer = crud_pokedex.get_pokemons(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to get data: {e}")

    return answer
