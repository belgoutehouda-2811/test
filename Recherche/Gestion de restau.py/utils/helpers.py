import os
import sys
from datetime import datetime, timedelta


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def afficher_titre(titre):
    print("\n" + "=" * 60)
    print(titre.center(60))
    print("=" * 60)


def saisir_entier(prompt, min_val=None, max_val=None):
    while True:
        try:
            valeur = int(input(prompt))
            if min_val is not None and valeur < min_val:
                print(f"La valeur doit être >= {min_val}")
                continue
            if max_val is not None and valeur > max_val:
                print(f"La valeur doit être <= {max_val}")
                continue
            return valeur
        except ValueError:
            print("Veuillez entrer un nombre valide")


def saisir_decimal(prompt, min_val=None):
    while True:
        try:
            valeur = float(input(prompt))
            if min_val is not None and valeur < min_val:
                print(f"La valeur doit être >= {min_val}")
                continue
            return valeur
        except ValueError:
            print("Veuillez entrer un nombre décimal valide")


def menu_choix(options, titre="MENU"):
    afficher_titre(titre)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print("-" * 60)

    choix = saisir_entier("Votre choix: ", 1, len(options))
    return choix


def confirmer_action(message="Confirmer l'action? (O/N): "):
    reponse = input(message).upper()
    return reponse == 'O'


def formater_date(date_obj):
    return date_obj.strftime("%d/%m/%Y %H:%M")


def calculer_tva(montant_ht, taux=0.10):
    return montant_ht * taux