from typing import ClassVar
import label


class Product:
    products: list = []

    @classmethod
    def get_price(cls, _index:int) -> int:
        return cls.products[_index][2]

    def __init__(self, _name:str, _stock:int, _price:int, _is_unit:bool):
        self.name:str = _name
        self.stock:int = _stock
        self.price:int = _price
        self.is_unit:bool = _is_unit
        Product.products.append([_name, _stock, _price, _is_unit])