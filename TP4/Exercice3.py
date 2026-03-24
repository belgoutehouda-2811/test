#Exercice 3 :
#  L’objectif est de remplir un liste L avec n entiers,
#  puis afficher le contenu de L.
#Correction

n=int(input("Combien de d entiers voulez vous saisir:"))
l=[]
for i in range (n):
    e=int(input("Entrez l entire {i+1}"))
    l.append(e)
print("Votre liste",l)