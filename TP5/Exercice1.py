#open("notes.txt","w+")
import csv 
fichier = open
nom_fichier = input("Entrez le nom du fichier : ")


with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            lignes = fichier.readlines()
            print("Contenu du fichier :")
            for ligne in lignes:
                print(ligne.strip())