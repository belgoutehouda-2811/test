import csv

with open("achats.csv", encoding="utf-8-sig") as f:
    lecteur = csv.DictReader(f, delimiter='|')
    total_revenu = 0
    categories_volume = {}
    categories_chiffre = {}
    clients_depenses = {}
    paiements = {}
    achats_mars = []

    for ligne in lecteur:
        if not ligne['Total']:
            continue

        prix = float(ligne['Price'])
        quantite = int(ligne['Quantity'])
        total = float(ligne['Total'])
        categorie = ligne['Category']
        client = ligne['CustomerID']
        paiement = ligne['PaymentMethod']
        date = ligne['Date']

        total_revenu += total
        categories_volume[categorie] = categories_volume.get(categorie, 0) + quantite
        categories_chiffre[categorie] = categories_chiffre.get(categorie, 0) + total
        clients_depenses[client] = clients_depenses.get(client, 0) + total
        paiements[paiement] = paiements.get(paiement, 0) + 1
        if date.startswith("2023-03"):
            achats_mars.append(ligne)

print("Contenu du fichier :")
for achat in achats_mars:
    print(achat)

print("Revenus totaux :", round(total_revenu, 2))
print("Catégories les plus vendues (volume) :", categories_volume)
print("Catégories les plus rentables :", categories_chiffre)
print("Client le plus dépensier :", max(clients_depenses, key=clients_depenses.get))
print("Modes de paiement utilisés :", paiements)
print("Achats en mars 2023 :")
for achat in achats_mars:
    print(f"{achat['Date']} - {achat['Product']} - {achat['Total']}")