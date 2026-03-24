#Exercice 8 : 
# On veut comparer les deux listes L1 et L2 et afficher ‘ Listes identiques’ 
# si on a le même contenu dans les deux listes et ‘ listes non identiques ‘ sinon. 
# Exemple d’exécution :
#  Remplir L1 : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#  Remplir L2 : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
# Résultat : Listes identiques
#Correction
L1 = []
L2 = []
x = int(input("Entrez la longueur de L1 : "))
for i in range(x):
    val = int(input(f"Entrez l'élément {i+1} de L1 : "))
    L1.append(val)
y = int(input("Entrez la longueur de L2 : "))
for i in range(y):
    val = int(input(f"Entrez l'élément {i+1} de L2 : "))
    L2.append(val)
if L1 == L2:
    print("Les listes sont identiques")
else:
    print("Les listes ne sont pas identiques")