#Exercice 18 :
#Écrire un programme avec une fonction moyenne() qui :
#1. Demande à l’utilisateur le nombre de notes.
#2. Demande à entrer chaque note;
#3. Calcule et retourne la moyenne.
#4. Affiche un message :
#- “Excellent” si la moyenne ≥ 16
#- “Bien” si moyenne ≥ 12
#- “Insuffisant” sinon
#correction
def moyenne():
    try:
        n = int(input("Combien de notes voulez-vous entrer ? "))
        if n <= 0:
            print("Le nombre de notes doit être supérieur à zéro.")
            return

        total = 0
        for i in range(n):
            note = float(input(f"Entrez la note {i+1} : "))
            total += note

        moy = total / n
        print(f"Moyenne : {moy:.2f}")

        if moy >= 16:
            print("Excellent")
        elif moy >= 12:
            print("Bien")
        else:
            print("Insuffisant")

    except ValueError:
        print("Entrée invalide. Veuillez entrer des nombres uniquement.")

moyenne()