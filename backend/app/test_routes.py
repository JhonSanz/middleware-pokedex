import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_pokemon_success():
    response = client.get("/pokedex/pikachu")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "pikachu"


def test_get_pokemon_not_found():
    response = client.get("/pokedex/unknownpokemon")
    assert response.status_code == 400


def test_update_pokemon_success():
    update_data = {"name": "Raichu"}
    response = client.put("/pokedex/pikachu", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Raichu"


def test_update_pokemon_not_found():
    update_data = {"name": "Raichu"}
    response = client.put("/pokedex/unknownpokemon", json=update_data)
    assert response.status_code == 400


def test_get_pokemons_success():
    response = client.get("/pokedex/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 10


def test_get_pokemons_pagination():
    response = client.get("/pokedex/?skip=10&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 5
