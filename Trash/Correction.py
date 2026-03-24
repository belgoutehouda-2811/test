import csv

# Lecture du fichier CSV
with open("achats.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='|')
    data = list(reader)

# Affichage de chaque ligne
for row in data:
    print(row)

# Calcul du revenu total
total = sum(float(e['total']) for e in data)
print(f"Revenus total: {total}$")

# Répartition des revenus par catégorie
category = {}
for element in data:
    cat = element['category']
    tot = float(element['total'])
    category[cat] = category.get(cat, 0) + tot

# Top 5 des catégories les plus rentables
top_categories = sorted(category.items(), key=lambda a: a[1], reverse=True)[:5]
print("Top 5 catégories :")
for cat, val in top_categories:
    print(f"{cat}: {val}$")

# Répartition des revenus par client
client = {}
for element in data:
    cus = element['customerID']
    tot = float(element['total'])
    client[cus] = client.get(cus, 0) + tot

# Client ayant généré le plus de revenus
top_client = max(client.items(), key=lambda a: a[1])
print(f"Top client : {top_client[0]} avec {top_client[1]}$")