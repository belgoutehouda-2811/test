#Exercice 5 :
#Lire la suite des prix (en dhs entiers et terminée par zéro) des achats d’un client. 
# Calculer la somme qu’il doit, lire la somme qu’il paye, et déterminer le reste à rendre



somme_totale = 0

print("Entrez les prix des articles (0 pour terminer) :")
while True:
    prix = int(input("Prix : "))
    if prix == 0:
        break
    somme_totale += prix
print("Somme totale à payer :", somme_totale, "Dhs")
somme_payee = int(input("Somme payée par le client : "))
reste = somme_payee - somme_totale
if reste < 0:
    print("Le client n'a pas payé assez. Il manque", abs(reste), "Dhs.")
else:
    print("Reste à rendre au client :", reste, "Dhs")