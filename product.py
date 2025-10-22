from typing import ClassVar
import label


class Product:
    products: list = []

    @classmethod
    def get_price(cls, _index:int, _amount) -> int:
        price = cls.products[_index][2]
        price *= _amount

        if cls.products[_index][3] is False:
            price /= 1000

        return price

    def __init__(self, _name:str, _stock:int, _price:float, _is_unit:bool):
        self.name:str = _name
        self.stock:int = _stock
        self.price:float = _price
        self.is_unit:bool = _is_unit
        Product.products.append([_name, _stock, _price, _is_unit])