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
        Product("Choux de Bruxelles", 4, 4, False),
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

    def __init__(self, _product:Product):
        self.product = _product

        #Product.products.append([_name, _stock, _price, _is_unit])