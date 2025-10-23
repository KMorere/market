#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shop import Shop
from client import Client

products = Shop.products
new_shop = Shop()
reader = ""


while True:
    new_client = Client(input("Entrez votre prénom : "), input("Entrez votre nom : "))

    while reader.lower() != "stop":
        print("Saisir 'Stop' pour terminer ses achats.")
        reader = input("Choisissez un produit : ").lower()

        if new_shop.get_product(reader):
            reader_amount = input("Quantité à acheter : ")
            new_client.buy(new_shop, new_shop.get_product(reader).name, int(reader_amount))  # type: ignore

    new_client.print_buy_list()
