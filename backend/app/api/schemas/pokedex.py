from pydantic import BaseModel
from typing import List, Optional


class PokedexBase(BaseModel):
    name: str
    id: int
    abilities: List[dict]
    sprites: dict
    types: List[dict]


class PokedexAll(BaseModel):
    name: str
    url: str


class PokedexUpdate(BaseModel):
    name: Optional[str] = None
    id: Optional[int] = None


class PokedexOut(PokedexBase):
    id: int

    class Config:
        orm_mode = True
