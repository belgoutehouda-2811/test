import csv
from datetime import datetime
from collections import defaultdict


def exercice4():
    try:
        with open('achats.csv', 'r', encoding='utf-8') as fichier:
            lecteur = csv.DictReader(fichier, delimiter='|')


            print("Contenu du fichier :")
            lignes = list(lecteur)
            for ligne in lignes[:5]:
                print(ligne)


            revenus_totaux = sum(float(ligne['Total']) for ligne in lignes)
            print(f"\nRevenus totaux : {revenus_totaux:.2f} €")
            categories_volume = defaultdict(int)
            categories_ca = defaultdict(float)

            for ligne in lignes:
                categorie = ligne['Category']
                quantite = int(ligne['Quantity'])
                total = float(ligne['Total'])

                categories_volume[categorie] += quantite
                categories_ca[categorie] += total

            print("\nCatégories par volume :")
            for categorie, volume in sorted(categories_volume.items(), key=lambda x: x[1], reverse=True):
                print(f"  {categorie}: {volume} unités")

            print("\nCatégories par chiffre d'affaires :")
            for categorie, ca in sorted(categories_ca.items(), key=lambda x: x[1], reverse=True):
                print(f"  {categorie}: {ca:.2f} €")

            depenses_clients = defaultdict(float)
            for ligne in lignes:
                client = ligne['CustomerID']
                total = float(ligne['Total'])
                depenses_clients[client] += total

            client_max = max(depenses_clients.items(), key=lambda x: x[1])
            print(f"\nClient le plus dépensier : {client_max[0]} avec {client_max[1]:.2f} €")
            paiements = defaultdict(int)
            for ligne in lignes:
                methode = ligne['PaymentMethod']
                paiements[methode] += 1

            print("\nModes de paiement :")
            for methode, count in paiements.items():
                print(f"  {methode}: {count} utilisations")
            print("\nAchats de mars 2023 :")
            for ligne in lignes:
                date_achat = datetime.strptime(ligne['Date'], '%Y-%m-%d')
                if date_achat.year == 2023 and date_achat.month == 3:
                    print(f"  {ligne['Date']} - {ligne['Product']} - {ligne['Total']} €")

    except FileNotFoundError:
        print("Le fichier 'achats.csv' n'existe pas")
    except Exception as e:
        print(f"Erreur : {e}")
