import product


class Label:
    def __init__(self, _name: str, _stock: int, _price: int, _is_unit: bool):
        self.name: str = _name
        self.stock: int = _stock
        self.price: int = _price
        self.is_unit: bool = _is_unit