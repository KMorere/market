#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shop import Shop
from client import Client

products = Shop.products
new_shop = Shop()
clients: list[Client] = new_shop.clients


def new_client_buy_session():
    reader = ""
    new_client = Client(input("Entrez votre prénom : "), input("Entrez votre nom : "))

    while reader.lower() != "stop":
        print("Saisir 'Stop' pour terminer ses achats.")
        reader = input("Choisissez un produit : ").lower()

        if new_shop.get_product(reader):
            reader_amount = input("Quantité à acheter : ")

            if reader_amount.isdigit():
                new_client.buy(new_shop, new_shop.get_product(reader).name, int(reader_amount))  # type: ignore
            else:
                print(f"Erreur, '{reader_amount}' n'est pas une entrée valide.")

    new_client.print_buy_list()

    input_str = input("Voulez vous ajouter un nouveau client ? (Oui/Non)")
    if input_str.lower() == "oui":
        new_client_buy_session()


if __name__ == '__main__':

    while True:
        new_client_buy_session()
        answer_str = input("Voulez vous imprimer la recette de la journée ? (Oui/Non)\n")

        if answer_str.lower() == "oui":
            for client in clients:
                client.print_buy_list()

        print(f"Recette de la journée: {new_shop.money}€ | Nombre de clients: {len(new_shop.clients)}")
        break