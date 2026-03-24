#Exercice 16 :
#Créer une fonction calcul(a, b, operateur) qui : 
# additionne si operateur vaut '+', 
# soustrait si '-',
#  multiplie si '*',
#  divise si '/' et affiche le résultat.
#Correction
def calcul(a, b, operateur):
    if operateur == '+':
        resultat = a + b
    elif operateur == '-':
        resultat = a - b
    elif operateur == '*':
        resultat = a * b
    elif operateur == '/':
        if b != 0:
            resultat = a / b
        else:
            print("Erreur : division par zéro.")
            return
    else:
        print("Opérateur non reconnu.")
        return

    print("Résultat :", resultat)