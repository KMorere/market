from typing import ClassVar
from product import Product


class Shop:
    """ Classe qui garde une liste de tous les produits en vente. """
    products: ClassVar[list["Product"]] = [
        Product("Clémentine", 6, 2.9, False),
        Product("Datte", 4, 7, False),
        Product("Grenade", 3, 3.5, False),
        Product("Kaki", 3, 4.5, False),
        Product("Kiwi", 5, 3.5, False),
        Product("Mandarine", 6, 2.8, False),
        Product("Orange", 8, 1.5, False),
        Product("Pamplemousse", 8, 2, True),
        Product("Poire", 5, 2.5, False),
        Product("Pomme", 8, 1.5, False),

        Product("Carotte", 7, 1.3, False),
        Product("Choux de Bx", 4, 4, False),
        Product("Chou vert", 12, 2.5, True),
        Product("Courge", 6, 2.5, True),
        Product("Endive", 5, 2.5, False),
        Product("Epinard", 4, 2.6, False),
        Product("Poireau", 5, 1.2, False),
        Product("Potiron", 6, 2.5, True),
        Product("Radis Noir", 10, 5, True),
        Product("Salsifis", 3, 2.5, False)
    ]


    @classmethod
    def get_price(cls, _index:int, _amount) -> float:
        """ Method used to get the price of a Product instance by its amount.

        :param _index: Get the specific index of a product from the products list. [!] TODO
        :param _amount: Amount of a specific product wanted.
        :return: Return the calculated price of the product from its price and amount.
        """
        price = cls.products[_index].price
        price *= _amount

        if cls.products[_index].is_unit is False:
            price /= 1000

        return price


    def __init__(self):
        self.display_products()


    @classmethod
    def remove_product(cls, _index:int, _amount):
        """ Permet d'enlever un produit une fois acheté. """
        cls.products[_index].stock -= _amount


    @classmethod
    def get_product(cls, _product_name:str) -> Product|None:
        """ Retourne un produit à partir de son nom. """
        product_dict = {cls.products[x].name.lower():cls.products[x] for x in range(len(cls.products))}

        return product_dict.get(_product_name)


    @classmethod
    def display_products(cls):
        print("Articles en vente : ")

        _tiny_width, _width = 3, 13
        _line = ''.join(['+' + '-' * (_width + 3)]) + ''.join(['+' + '-' * (_tiny_width + 5)]) \
                + ''.join(['+' + '-' * (_width + 1)]) + '+'

        print(_line)
        print(f"| Article        | Stock  | Prix         |")
        print(_line)

        for product in cls.products:
            _name, _quantity, _price = product.name, product.stock, product.price
            _total_line_price = round(_price * _quantity, 2)

            _quantity_display = '' + str(_quantity).center(1) + ' /'
            _price_display = ' ' + ''.join([str(_total_line_price) + ' €']).center(0) + ' /'

            price_type_str = "pc" if product.is_unit else "kg"

            line_display = (f"|{_name.center(_width)}   |"
                            f" {_quantity_display} {price_type_str} |"
                            f" {_price_display} {price_type_str} |")
            print(line_display)

        print(_line)