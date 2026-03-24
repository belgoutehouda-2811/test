#Exercice 7 :
#Écrire un programme qui demande à l’utilisateur de saisir des notes (sur 20) et calculer la moyenne.
# L'utilisateur continue de saisir des notes jusqu'à ce qu'il entre une note négative.
#  Ensuite, le programme affiche la moyenne des notes.

#Correction


somme = 0
compt = 0

while True:
    notes = float(input("Entrez votre note : "))
    if notes < 0:
        break
    somme += notes
    compt += 1

if compt > 0:
    moyenne = somme / compt
    print("Votre moyenne est :", moyenne)
else:
    print("Aucune note valide saisie.")
