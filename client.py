
from product import Product
from datetime import datetime
from shop import Shop

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
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.total_spent = 0.00
        self.buy_list = []


    def __repr__(self) -> str:
        return f"{self.last_name} {self.first_name}: {self.total_spent}€"


    def __str__(self) -> str:
        self.print_buy_list()
        return f"{self.last_name} {self.first_name} vous avez dépensé aujourd'hui: {self.total_spent}€"


    def print_buy_list(self):
        _date = datetime.today().strftime('%d-%m-%Y')
        _tiny_width, _width = 3,13
        _line = ''.join(['+' + '-' * (_tiny_width + 2)]) + ''.join(['+' + '-' * (_width + 2)])\
                + ''.join(['+' + '-' * (_tiny_width + 3)]) + '+'
        print(f"Édition du {_date} - Client {self.first_name} {self.last_name}")
        print(_line)
        print(f"| Qté |    Article    | Prix |")
        print(_line)
        _total_price = 0
        for buy in self.buy_list:
            _name, _quantity, _price = buy
            _total_line_price = round(_price * _quantity, 2)
            _total_price += _total_line_price
            _quantity_display = '  ' + str(_quantity).center(_tiny_width) + '  '
            _price_display = ' ' + ''.join([str(_total_line_price) + '€']).center(_tiny_width+2) + '  '
            line_display = f"{_quantity_display} {_name.center(_width)} {_price_display}"
            print(line_display)
        print(_line)
        print(f"| Total                 {_total_price}€  |")
        print(_line)

    @staticmethod
    def can_buy(_product: Product, _quantity:float) -> bool:
        """ Checks if `_product` is_unit and returns True if `_product` is available, False otherwise """
        return _quantity <= _product.stock if _product.is_unit else _quantity / 1000 <= _product.stock


    def buy(self, _shop: Shop, _product: Product, _quantity: float):
        """
        Checks if `can_buy`, if True compute price, remove it from stock and adds it to history,
        Prints an error message otherwise.
        """
        if self.can_buy(_product, _quantity):
            # self.total_spent += _shop.get_price(_product.price)
            self.buy_list.append((_product.name, _quantity, _product.price))
            # _product.stock -= int(round(_quantity))
        else:
            print(f"Le produit {_product.name} n'a pas un stock suffisant pour cet achat. (dispo : {_product.stock})\n")
client = Client("toto", "titi")



produits = Shop.products
shop = Shop(produits[0])

client.buy(shop, produits[0], 1)
client.buy(shop, produits[1], 3)
client.buy(shop, produits[1], 8)
client.print_buy_list()
