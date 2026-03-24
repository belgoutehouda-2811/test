#Exercice 11 :
#  Une matrice est dite matrice carrée si elle a le même nombre de lignes et de colonnes.
#  Proposer un programme qui permet de remplir et afficher une matrice carrée de taille n
#  ( càd : l=c=n).
#  l et c sont saisis au clavier.
#Correction
n = int(input("Entrez la taille n de la matrice carrée : "))

matrice = []

for i in range(n):
    ligne = []
    for j in range(n):
        val = int(input(f"Entrez l'élément [{i}][{j}] : "))
        ligne.append(val)
    matrice.append(ligne)

print("\nMatrice carrée :")
for ligne in matrice:
    print(ligne)