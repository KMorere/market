from dataclasses import dataclass
from typing import ClassVar

from product import Product


@dataclass
class Client:
    first_name: str
    last_name: str
    total_spent: float
    buy_list: ClassVar[Product]


    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.total_spent = 0


    def __repr__(self):
        return f"{self.last_name} {self.first_name}: {self.total_spent}€"


    def __str__(self):
        return f"Client {self.last_name} {self.first_name}, Total dépensé aujourd'hui: {self.total_spent}"


    def buy_product(self, product: Product):
        ...

