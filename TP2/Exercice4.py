#Exercice 4 :
#Écrire un programme qui demande à l’utilisateur de saisir des nombres positifs. 
# Le programme se termine lorsque l’utilisateur saisit un nombre négatif. 
# Afficher la somme de tous les nombres positifs saisis.


#correction

somme=0
#n=int(input("Entrez le nombre"))
while True :
 
 n=int(input("Entrez le nombre"))
 
 if n<0:
  break
 somme+=n
print ("la somme des nombres est",somme)