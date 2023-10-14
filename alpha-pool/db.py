from dataclasses import dataclass
from typing import List


@dataclass(frozen=True, slots=True)
class AlphaSource:
    name: str
    description: str
    source: str
    year: int
    tags: List[str]


records = [
    AlphaSource(name=""),
]