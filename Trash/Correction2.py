import csv
import datetime

with open("achats.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='|')
    data = list(reader)

for row in data:
    print(row)

total = sum(float(e['Total']) for e in data)
print(f"Revenues Total: {total}$")

category = {}
for e in data:
    cat = e['category']
    tot = float(e['Total'])
    category[cat] = category.get(cat, 0) + tot

client = {}
for e in data:
    cus = e['customerID']
    tot = float(e['Total'])
    client[cus] = client.get(cus, 0) + tot

topclient = max(client.items(), key=lambda x: x[1])
print(f"Client ayant dépensé le plus : {topclient[0]} avec {topclient[1]}$")

topcategory = max(category.items(), key=lambda x: x[1])
print(f"Catégorie la plus vendue (CA): {topcategory[0]} avec {topcategory[1]}$")

paiement = {}
for e in data:
    method = e['paymentmethod']
    paiement[method] = paiement.get(method, 0) + 1

top_paiement = max(paiement.items(), key=lambda x: x[1])
print(f"Mode de paiement le plus utilisé : {top_paiement[0]} ({top_paiement[1]} fois)")

print("\nAchats en mars 2023 :")
for e in data:
    d = datetime.datetime.strptime(e['date'], "%Y-%m-%d")
    if d.year == 2023 and d.month == 3:
        print(e)