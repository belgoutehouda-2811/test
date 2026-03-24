#Exercice 19 :
#Créer une fonction factoriel(n) qui retourne le factoriel d’un nombre n (avec une boucle).
#Page :
def factoriel(n):
    if n < 0:
        return "Le factoriel n'est pas défini pour les entiers négatifs."
    
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat