from pydantic import BaseModel
from typing import List, Optional


class PokedexBase(BaseModel):
    name: str
    abilities: List[dict]
    id: int
    sprites: dict
    types: List[dict]


class PokedexAll(BaseModel):
    name: str
    url: str


class PokedexCreate(PokedexBase):
    pass


class PokedexUpdate(PokedexBase):
    pass


class PokedexOut(PokedexBase):
    id: int

    class Config:
        orm_mode = True
