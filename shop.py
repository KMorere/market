from typing import ClassVar
from product import Product


class Shop:
    products: ClassVar[list["Product"]] = [
        Product("Pomme", 3, 1, False),
        Product("Orange", 3, 1, False),
    ]

    @classmethod
    def get_price(cls, _index:int, _amount) -> int:
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