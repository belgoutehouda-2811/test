def calculatrice():
    while True:
        print("\n--- CALCULATRICE ---")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulo (%)")
        print("0. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "0":
            print("Fin du programme.")
            break

        # Demander les nombres
        try:
            a = float(input("Entrez le premier nombre : "))
            b = float(input("Entrez le deuxième nombre : "))
        except ValueError:
            print("Erreur : veuillez entrer des nombres valides.")
            continue

        # Calcul selon le choix
        if choix == "1":
            print("Résultat :", a + b)
        elif choix == "2":
            print("Résultat :", a - b)
        elif choix == "3":
            print("Résultat :", a * b)
        elif choix == "4":
            if b == 0:
                print("Erreur : division par zéro impossible.")
            else:
                print("Résultat :", a / b)
        elif choix == "5":
            if b == 0:
                print("Erreur : modulo par zéro impossible.")
            else:
                print("Résultat :", a % b)
        else:
            print("Option invalide. Réessayez.")

# Lancer la calculatrice
calculatrice()