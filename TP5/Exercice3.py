import csv

def lire_csv_et_trouver_majorant():
    nom_fichier = input("Entrez le nom du fichier CSV (ex: notes.csv) : ")

    try:
        with open(nom_fichier, newline='', encoding='utf-8-sig') as fichier:
            lecteur = csv.DictReader(fichier)
            eleves = list(lecteur)

            if not eleves:
                print("Le fichier est vide.")
                return

            print("\n📋 Contenu du fichier :")
            for eleve in eleves:
                print(f"{eleve['Nom']} {eleve['Prénom']} - Note : {eleve['Note']}")

            majorant = max(eleves, key=lambda e: float(e['Note']))

            print("\n Élève ayant la meilleure note :")
            print(f"{majorant['Nom']} {majorant['Prénom']} - Note : {majorant['Note']}")

    except FileNotFoundError:
        print(" Fichier introuvable. Vérifiez le nom et réessayez.")
    except KeyError:
        print(" Le fichier ne contient pas les colonnes attendues : Nom, Prénom, Note.")
    except Exception as e:
        print(f" Une erreur est survenue : {e}")

lire_csv_et_trouver_majorant()

#fichier = input("Nom du fichier")
#meilleur = None
#with open(fichier) as f:
#    for ligne in f:
#        ligne = ligne.strip().split()
#        print(ligne)
#        if meilleur is None or float(ligne[3]) > float(meilleur[3]):
#            meilleur = ligne 
#print("Meilleur élève:",meilleur)