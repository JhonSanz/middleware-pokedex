import requests


def get_pokemon(*, pokemon_identifier: str) -> dict:
    pokemons = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}",
        # params={"skip"}
    )
    print(pokemons)
    return pokemons.json()
