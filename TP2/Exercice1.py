#Exercice 1 :
#A partir d’un montant lu, on détermine un montant net par application d’une remise de :
#- 1% si le montant est compris entre 2000 et 5000 Dhs (valeurs comprises)
#- 2 % si le montant est supérieur à 5000 Dhs.

#Correction
montant = float(input("Entrez le Montant en dhs"))
montant_net = float
remise = float
if 2000<montant and montant<5000 :
  remise = montant*0.01
elif montant>5000:
  remise =montant*0.02
else:
  remise = 0
montant_net= montant - remise

print("Votre montant net est:",montant_net , "dhs")

