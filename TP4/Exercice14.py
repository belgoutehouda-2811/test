#Methode 1
chaine = input("Entrez une chaîne de chiffres : ")
nouvelle_chaine = ""

for caractere in chaine:
    if caractere == '0':
        nouvelle_chaine += 'x'
    else:
        nouvelle_chaine += caractere

print("Chaîne modifiée :", nouvelle_chaine)
#methode 2
chaine = input("Entrez une chaîne de chiffres : ")
nouvelle_chaine = ""

for caractere in chaine:
    if caractere == '0':
        nouvelle_chaine += 'x'
        continue
    nouvelle_chaine += caractere

print("Chaîne modifiée :", nouvelle_chaine)