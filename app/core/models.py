from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Car:
    code: int
    model: str
    notes: Optional[str] = None


@dataclass
class Brand:
    code: str
    name: str
    cars: List[Car]
