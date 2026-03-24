import json

nom_fichier = input("Entrez le nom du fichier JSON : ")

try:
    with open(nom_fichier, encoding='utf-8') as f:
        etudiants = json.load(f)

    for e in etudiants:
        print(f"{e['code']} - {e['prenom']} {e['nom']} : {e['note']}")

    majorant = max(etudiants, key=lambda e: e['note'])
    print(f"\nMeilleur étudiant : {majorant['code']} - {majorant['prenom']} {majorant['nom']} : {majorant['note']}")

    moyenne = sum(e['note'] for e in etudiants) / len(etudiants)
    print("Moyenne :", round(moyenne, 2))

    au_dessus = [e for e in etudiants if e['note'] > moyenne]
    print("Nombre au-dessus de la moyenne :", len(au_dessus))

    triés = sorted(etudiants, key=lambda e: e['note'], reverse=True)
    print("\nÉtudiants triés par note décroissante :")
    for e in triés:
        print(f"{e['code']} - {e['prenom']} {e['nom']} : {e['note']}")

except:
    print("Erreur lors de la lecture du fichier.")