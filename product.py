from typing import ClassVar
import product_label


class Product:
    products: ClassVar[list["Product"]] = []

    @classmethod
    def get_price(cls, _product:int) -> int:
        return cls.products[_product].price

    def __init__(self, _name:str, _stock:int, _price:int, _is_unit:bool):
        self.name:str = _name
        self.stock:int = _stock
        self.price:int = _price
        self.is_unit:bool = _is_unit
        Product.products.append(self)


new_prod = Product("Pomme", 3, 1, True)
print(new_prod.name)
print(Product.products[0])