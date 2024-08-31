import requests
from app.api.schemas.pokedex import PokedexUpdate


def get_pokemon(*, pokemon_identifier: str) -> dict:
    pokemons = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}",
    )
    if not pokemons:
        raise Exception("Pokemon not found :(")

    return pokemons.json()


def get_pokemons(*, skip: int = 0, limit: int = 10) -> dict:
    pokemons = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/",
        params={"offset": skip, "limit": limit},
    )
    return pokemons.json()["results"]


def update_pokemon(*, pokemon_identifier: str, pokemon_data: PokedexUpdate):
    current_pokemon = get_pokemon(pokemon_identifier=pokemon_identifier)

    update_data = {
        key: value for key, value in pokemon_data.model_dump().items() if value is not None
    }
    current_pokemon.update(update_data)
    return current_pokemon
