from product import Product


class Client:
    first_name: str
    last_name: str
    total_spent: float
    buy_list: list[tuple[string, float]]


    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.total_spent = 0.00
        self.buy_list = []


    def __repr__(self) -> str:
        return f"{self.last_name} {self.first_name}: {self.total_spent}€"


    def __str__(self) -> str:
        return f"Client {self.last_name} {self.first_name}, Total dépensé aujourd'hui: {self.total_spent}"


    @staticmethod
    def can_buy(_product: Product, _quantity:float):
        return _quantity >= _product.stock


    def buy(self, product: Product, quantity: float):
        if self.can_buy(product, quantity):
            self.total_spent += product.price
            self.buy_list.append((product.name, quantity))
        else:
            print(f"Le produit {product.name} n'a pas un stock suffisant pour cet achat. ({product.stock})")
