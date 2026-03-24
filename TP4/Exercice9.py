#Exercice 9 :
#Écrire un programme Python qui permet de supprimer les éléments dupliqués d’une liste.
#Correction
l = [1, 4, 5, 4, 10, 1, 22, 5, 30, 22]


l_sans_doublons = list(set(l))

print("Liste originale :", l)
print("Liste sans doublons :", l_sans_doublons)
