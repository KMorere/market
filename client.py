
from product import Product
from datetime import datetime
from shop import Shop

class Client:
    """
    A class that represent a customer with a `first_name` and `last_name` as identification,
    stores buying history in `buy_list` and compute `total_spent`

    Methods:
        is_available(product, quantity): Returns true if desired quantity is available, False otherwise
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
        """
        Prints out a formatted receipt of the records in the `buy_list`
        """
        _date = datetime.today().strftime('%d-%m-%Y')
        _tiny_width, _width = 3,13
        _line = ''.join(['+' + '-' * (_tiny_width + 2)]) + ''.join(['+' + '-' * (_width + 2)])\
                + ''.join(['+' + '-' * (_tiny_width + 3)]) + '+'
        print(f"{_date} - {self.first_name} {self.last_name}")
        print(_line)
        print(f"| Qté |    Article    | Prix |")
        print(_line)
        _total_price = 0
        for buy in self.buy_list:
            _name, _quantity, _price = buy
            _total_line_price = round(_price * _quantity, 2)
            _total_price += round(_total_line_price, 2)
            _quantity_display = '| ' + str(_quantity).center(_tiny_width) + ' |'
            _price_display = '|' + ''.join([str(_total_line_price) + '€']).center(_tiny_width+2) + ' |'
            line_display = f"{_quantity_display} {_name.center(_width)} {_price_display}"
            print(line_display)
        print(_line)
        print('| ' + 'Total: '.center(_width) + ''.join([_total_price.__str__() + '€']).center(_width) + ' |')
        print(_line)

    @staticmethod
    def is_available(_shop: type[Shop], _name: str, _quantity: float) -> bool:
        """ Checks if product is in stock in `_shop`, Returns True if available, False otherwise """
        return _quantity <= _shop.get_product(_name).stock

    def buy(self, _shop: type[Shop], _name: str, _quantity: float):
        """
        Checks if `is_available`, if True gets price from shop, remove it from stock and adds it to client history,
        Prints an error message otherwise.
        """
        _product = _shop.get_product(_name)
        if self.is_available(_shop, _product.name, _quantity):
            _shop.remove_product(_shop.products.index(_product), _quantity)
            self.total_spent += _shop.get_price(_shop.products.index(_product), _quantity)
            self.buy_list.append((_product.name, _quantity, _product.price))
        else:
            print(f"Le produit {_product.name} n'a pas un stock suffisant pour cet achat. (dispo : {_product.stock})\n")


client = Client("Albert", "Roquefort")

shop = Shop
clementine = shop.get_product("Clémentine")
client.buy(shop, clementine.name, 1)

client.print_buy_list()
