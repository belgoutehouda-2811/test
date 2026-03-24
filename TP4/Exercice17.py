#Exercice 17 :
#Créer une fonction est_palindrome(mot) qui retourne True si le mot est un palindrome, False sinon.
#Correction
def est_palindrome(mot):
    mot = mot.lower()  # Ignorer la casse
    mot = mot.replace(" ", "")  # Ignorer les espaces
    return mot == mot[::-1]