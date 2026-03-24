#Exercice 7 : On suppose qu’on a L une liste remplie par des réels. 
# On veut remplir deux listes L1 et L2 à partir de la liste L tel que :
#  1- les nombres pairs dans L seront copiés dans L1.
#  2- Le reste dans L2 Exemple d’exécution : 
# Donner le nombre des éléments à insérer : 10 
# Résultat : L : -9 1 6 14 -8 100 3 44 63 10 
# L1 : 6 14 -8 100 44 10 et L2 : -9 1 3 63
#Correction
n=int(input("entrez le nombres voulais dans la liste"))
l=[]
L1=[]
L2=[]
for i in range(n):
 x=int(input("Entrez le nombre des element a inserer"))
 l.append(x)

 if  x%2==0:
  L1.append(x)
 else:
  L2.append(x)

print("la liste initiale",l)
print("Laliste des pairs de l",L1)
print("Laliste des impairs de l",L2)