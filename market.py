from shop import Shop
from client import Client

products = Shop.products
new_shop = Shop()
new_client = Client("King", "Clawthorn")
reader = ""

while reader.lower() != "stop":
    reader = input("Choisissez un produit : ").lower()

    if new_shop.get_product(reader):
        reader_amount = input("Quantité à acheter : ")
        new_client.buy(new_shop, new_shop.get_product(reader), int(reader_amount))  # type: ignore

        print(f"Achat de {reader_amount} {reader}")

new_client.print_buy_list()