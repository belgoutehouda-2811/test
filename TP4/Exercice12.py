#Exercice 12 :
#  Soit une matrice A(n,m) de valeurs entières. 
# Ecrire un programme qui permet de faire un tri décroissant de la matrice A
#Correction
# Saisie des dimensions de la matrice
n = int(input("Entrez le nombre de lignes (n) : "))
m = int(input("Entrez le nombre de colonnes (m) : "))

A = []
for i in range(n):
    ligne = []
    for j in range(m):
        val = int(input(f"Entrez l'élément [{i}][{j}] : "))
        ligne.append(val)
    A.append(ligne)

elements = [val for row in A for val in row]

elements.sort(reverse=True)

A_triee = []
index = 0
for i in range(n):
    ligne = []
    for j in range(m):
        ligne.append(elements[index])
        index += 1
    A_triee.append(ligne)

print("\nMatrice initiale :")
for row in A:
    print(row)

print("\nMatrice triée en ordre décroissant :")
for row in A_triee:
    print(row)