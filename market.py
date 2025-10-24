#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shop import Shop
from client import Client

products = Shop.products
new_shop = Shop()
clients: list[Client] = []


def new_client_buy_session():
    reader = ""
    new_client = Client(input("Entrez votre prénom : "), input("Entrez votre nom : "))

    while reader.lower() != "stop":
        print("Saisir 'Stop' pour terminer ses achats.")
        reader = input("Choisissez un produit : ").lower()

        if new_shop.get_product(reader):
            reader_amount = input("Quantité à acheter : ")
            new_client.buy(new_shop, new_shop.get_product(reader).name, int(reader_amount))  # type: ignore

    clients.append(new_client)


while True:
    new_client_buy_session()

    input_str = input("Voulez vous ajouter un nouveau client ? (o/n)")
    if input_str == "o":
        new_client_buy_session()
    else:
        for client in clients:
            client.print_buy_list()
