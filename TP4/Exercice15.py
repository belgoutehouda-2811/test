#Exercice15
chaine = input("Entrez une chaîne de caractères : ")

for caractere in chaine:
    if caractere == 'o':
        break
    print(caractere, end='')

print()  # Pour aller à la ligne après l'affichage