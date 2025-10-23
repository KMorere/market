
from product import Product


class Client:
    """
    A class that represent a customer with a `first_name` and `last_name` as identification,
    stores buying history in `buy_list` and compute `total_spent`

    Methods:
        can_buy(product, quantity): Returns true if desired quantity is available, False otherwise
        buy(product, quantity): check if product is available, then buy it and add it to history
    """
    first_name: str
    last_name: str
    total_spent: float
    buy_list: list[tuple[str, float, float]]  # buy history eg: ('Banane', 8, 7.99)


    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.total_spent = 0.00
        self.buy_list = []


    def __repr__(self) -> str:
        return f"{self.last_name} {self.first_name}: {self.total_spent}€"


    def __str__(self) -> str:
        return (f"Client {self.last_name} {self.first_name}, Total dépensé aujourd'hui: {self.total_spent}€"
                f"{self.buy_list}")

    @staticmethod
    def can_buy(_product: Product, _quantity:float) -> bool:
        """ Checks if `_product` is_unit and returns True if `_product` is available, False otherwise """
        return _quantity <= _product.stock if _product.is_unit else _quantity / 1000 <= _product.stock


    def buy(self, product: Product, quantity: float):
        """
        Checks if `can_buy`, compute price and adds it to history if possible,
        Prints an error message otherwise.
        """
        if self.can_buy(product, quantity):
            if product.is_unit:
                self.total_spent += round(product.price * quantity, 2)  # rounds to 2 decimals
                self.buy_list.append((product.name, quantity, product.price))
            else:
                kilo_quantity = quantity / 1000
                self.total_spent += round(product.price * kilo_quantity, 2)
                self.buy_list.append((product.name, quantity, product.price))
        else:
            print(f"Le produit {product.name} n'a pas un stock suffisant pour cet achat. ({product.stock})")


client = Client("toto", "titi")

produit1 = Product("Orange", 8, 1.50, False)
produit2 = Product("Pamplemousse", 8, 2, True)

client.buy(produit1, 1000)
client.buy(produit2, 8)
print(client.__str__())
print('-' * 30)
print(client.__repr__())