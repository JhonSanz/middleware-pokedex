import requests


def get_pokemon(*, pokemon_identifier: str) -> dict:
    pokemons = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}",
    )
    return pokemons.json()


def get_pokemons(*, skip: int = 0, limit: int = 10) -> dict:
    pokemons = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/",
        params={"offset": skip, "limit": limit},
    )
    return pokemons.json()["results"]
