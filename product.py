from dataclasses import dataclass
from typing import ClassVar
from label import Label


@dataclass
class Product:
    products: ClassVar[list["Product"]] = [
        Label("Pomme", 3, 1, True),
        Label("Orange", 5, 1, True),
    ]

    @classmethod
    def get_price(cls, _product:int) -> int:
        return cls.products[_product].price

    def __init__(self, _name:str, _stock:int, _price:int, _is_unit:bool):
        self.name:str = _name
        self.stock:int = _stock
        self.price:int = _price
        self.is_unit:bool = _is_unit