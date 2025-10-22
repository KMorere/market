from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Product:
    products : ClassVar[list["Product"]] = []