#Exercice 4 : 
# Soit L une liste de N entiers (remplie par N entier). 
# On veut déterminer le plus petit élément de cette liste et sa position
#Correction
n=int(input("Entrez votre entier"))
l=[]
for i in range(n):
 e=int(input("Entrez le {i+1}"))
 l.append(e)

min_valeur = l[0]
position = 0

for i in range(1, n):
    if l[i] < min_valeur:
        min_valeur = l[i]
        position = i

print("la valeur min est:",min_valeur)
print(" ca position est:",position)