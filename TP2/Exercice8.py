#Exercice 8 :
#Écrire un programme qui affiche un menu avec plusieurs options
#(1 : additionner deux nombres, 2 : soustraire deux nombres, 3 : quitter).
#L'utilisateur choisit une option.
#  L'programme doit répéter le menu jusqu'à ce que l'utilisateur sélectionne "quitter".

while True:
    print("\nMenu :")
    print("1 : Additionner deux nombres")
    print("2 : Soustraire deux nombres")
    print("3 : Quitter")

    choix = input("Choisissez une option (1, 2 ou 3) : ")

    if choix == "1":
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))
        print("Résultat :", a + b)

    elif choix == "2":
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))
        print("Résultat :", a - b)

    elif choix == "3":
        print("Programme terminé. Au revoir !")
        break

    else:
        print("Option invalide. Veuillez choisir 1, 2 ou 3.")