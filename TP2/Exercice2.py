#Exercice 2 :
#Écrire un programme qui demande à l’utilisateur de saisir un nombre entier positif n, 
# puis affiche combien de nombres pairs se trouvent entre 1 et n.
 
#Correction
n = int(input("Entrez le nombre"))
if n<1:
    print("Le nombre doit etre positive")
else:
    n//2 
    print("Entra 1 et",n,",",n//2,"nombres pairs")