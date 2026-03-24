import csv
with open("achats.csv", encoding="utf-8-sig") as f:
    lecteur = csv.DictReader(f, delimiter='|')
    donnees = [ligne for ligne in lecteur if ligne['Total']]

print("Contenu du fichier :")
for ligne in donnees:
    print(ligne)

total_revenu = sum(float(ligne['Total']) for ligne in donnees)
print("Revenus totaux :", round(total_revenu, 2))

categories_volume = {}
categories_chiffre = {}

for ligne in donnees:
    categorie = ligne['Category']
    quantite = int(ligne['Quantity'])
    total = float(ligne['Total'])
    categories_volume[categorie] = categories_volume.get(categorie, 0) + quantite
    categories_chiffre[categorie] = categories_chiffre.get(categorie, 0) + total

print("Catégories les plus vendues (volume) :", categories_volume)
print("Catégories les plus rentables :", categories_chiffre)

clients_depenses = {}
for ligne in donnees:
    client = ligne['CustomerID']
    total = float(ligne['Total'])
    clients_depenses[client] = clients_depenses.get(client, 0) + total

client_top = max(clients_depenses, key=clients_depenses.get)
print("Client le plus dépensier :", client_top, "-", round(clients_depenses[client_top], 2))

paiements = {}
for ligne in donnees:
    methode = ligne['PaymentMethod']
    paiements[methode] = paiements.get(methode, 0) + 1

print("Modes de paiement utilisés :", paiements)

achats_mars = [ligne for ligne in donnees if ligne['Date'].startswith("2023-03")]

print("Achats en mars 2023 :")
for achat in achats_mars:
    print(f"{achat['Date']} - {achat['Product']} - {achat['Total']}")