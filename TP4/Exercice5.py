#Exercice 5 : 
# Soit L une liste de N réels.
#  L’objectif est de calculer le nombre des occurrences d’un nombre X 
# (c’est-à-dire combien de fois ce nombre X figure dans la liste L).
#Correction
n=int(input("Entrez l entiers "))
l=[]

for i in range (n):
    e=int(input("Entrez les entiers{i+1}"))
    l.append(e)

x = float(input("Entrez le nombre X à rechercher : "))

occurrences = l.count(x)
print(f"Le nombre {x} apparaît {occurrences} fois dans la liste.")
