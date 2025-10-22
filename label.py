from product import Product


class Label(Product):
    def __init__(self, _name: str, _stock: int, _price: int, _is_unit: bool):
        super().__init__(_name, _stock, _price, _is_unit)

        self.name: str = _name
        self.stock: int = _stock
        self.price: int = _price
        self.is_unit: bool = _is_unit