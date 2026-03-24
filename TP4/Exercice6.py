#Exercice 6 : 
# On suppose que la liste L est déjà remplie et ordonnée.
#  On va : 
# – Demander un nombre à insérer 
# – Insérer le nombre dans la position adéquate 
# (c à d, de telle façon à ce que la liste reste ordonné)
# – Affiche la liste après insertion du nouveau nombre Exemple d’exécution :
#  Remplissage de L : 1 4 5 10 20 22 25 30 32 Donner x : 7 
# L après insertion : 1 4 5 7 10 20 22 25 30 32
#Correction

l = [1, 4, 5, 10, 20, 22, 25, 30, 32]

print("Liste initiale :", l)

x = int(input("Donner x : "))

l.append(x)
l.sort()

print("l après insertion :", l)
