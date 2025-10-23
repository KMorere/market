
from product import Product


class Client:
    first_name: str
    last_name: str
    total_spent: float
    buy_list: list[tuple[str, float, float]]


    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.total_spent = 0.00
        self.buy_list = []


    def __repr__(self) -> str:
        return f"{self.last_name} {self.first_name}: {self.total_spent}€"


    def __str__(self) -> str:
        return (f"Client {self.last_name} {self.first_name}, Total dépensé aujourd'hui: {self.total_spent}€"
                f"--------" * 10 +
                f"{self.buy_list.__str__()}")


    @staticmethod
    def can_buy(_product: Product, _quantity:float):
        return _quantity >= _product.stock


    def buy(self, product: Product, quantity: float):
        if self.can_buy(product, quantity):
            if product.is_unit:
                self.total_spent += product.price * quantity
                self.buy_list.append((product.name, quantity, product.price))
            else:
                kilo_quantity = quantity / 1000
                self.total_spent += product.price * kilo_quantity
                self.buy_list.append((product.name, quantity, product.price))
        else:
            print(f"Le produit {product.name} n'a pas un stock suffisant pour cet achat. ({product.stock})")
