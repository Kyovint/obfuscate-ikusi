from typing import Any
from pydantic import BaseModel


class ObfuscateRequest(BaseModel):
    columns: list[str]
    rows: list[list[Any]]


class ObfuscateResponse(BaseModel):
    columns: list[str]
    rows: list[list[Any]]
