import csv
import os

FICHIER = "etudiants.csv"

# Initialiser le fichier si vide
if not os.path.exists(FICHIER):
    with open(FICHIER, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Nom", "Prenom", "DateNaissance", "Cours"])

def ajouter_etudiant():
    id_etudiant = input("ID : ")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
    cours = input("Cours : ")

    with open(FICHIER, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([id_etudiant, nom, prenom, date_naissance, cours])
    print("Étudiant ajouté avec succès.")

def afficher_etudiants():
    with open(FICHIER, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for ligne in reader:
            print(ligne)

def rechercher_etudiant():
    id_recherche = input("Entrez l'ID de l'étudiant : ")
    with open(FICHIER, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for ligne in reader:
            if ligne["ID"] == id_recherche:
                print("Étudiant trouvé :", ligne)
                return
    print("Étudiant introuvable.")

def supprimer_etudiant():
    id_supprimer = input("Entrez l'ID de l'étudiant à supprimer : ")
    lignes = []
    with open(FICHIER, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for ligne in reader:
            if ligne["ID"] != id_supprimer:
                lignes.append(ligne)

    with open(FICHIER, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "Nom", "Prenom", "DateNaissance", "Cours"])
        writer.writeheader()
        writer.writerows(lignes)
    print("Étudiant supprimé.")

def mettre_a_jour_etudiant():
    id_update = input("Entrez l'ID de l'étudiant à mettre à jour : ")
    lignes = []
    updated = False
    with open(FICHIER, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for ligne in reader:
            if ligne["ID"] == id_update:
                print("Étudiant trouvé :", ligne)
                ligne["Nom"] = input("Nouveau nom : ")
                ligne["Prenom"] = input("Nouveau prénom : ")
                ligne["DateNaissance"] = input("Nouvelle date de naissance (AAAA-MM-JJ) : ")
                ligne["Cours"] = input("Nouveau cours : ")
                updated = True
            lignes.append(ligne)

    with open(FICHIER, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "Nom", "Prenom", "DateNaissance", "Cours"])
        writer.writeheader()
        writer.writerows(lignes)

    if updated:
        print("Étudiant mis à jour.")
    else:
        print("Étudiant introuvable.")

def menu():
    while True:
        print("\n--- MENU GESTION ÉTUDIANTS ---")
        print("1. Ajouter un étudiant")
        print("2. Afficher tous les étudiants")
        print("3. Rechercher un étudiant")
        print("4. Supprimer un étudiant")
        print("5. Mettre à jour un étudiant")
        print("0. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            ajouter_etudiant()
        elif choix == "2":
            afficher_etudiants()
        elif choix == "3":
            rechercher_etudiant()
        elif choix == "4":
            supprimer_etudiant()
        elif choix == "5":
            mettre_a_jour_etudiant()
        elif choix == "0":
            print("Fin du programme.")
            break
        else:
            print("Option invalide.")

menu()