#Exercice 3 :
#Écrire un programme qui demande à l’utilisateur de saisir un mot de passe.
#  Tant que le mot de passe est incorrect, le programme redemande la saisie.
#  Si le mot de passe est correct, afficher "Accès autorisé".

#Correction

password=int(input("Entrez votre mot de passe"))
p=0000
while password!=p:
 print("Votre mot de passe est incorrect")
 password=int(input("Entrez votre mot de passse"))
print("Accès autorisé")