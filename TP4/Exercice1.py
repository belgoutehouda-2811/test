#Exercice 1 : 
# Ecrire un programme en python qui calcule le volume d’une sphère étant donné son rayon, sachant que :
# V = 4/3( πR3).

#Correction

import math

def volume_sphere(r) :
 return  (4/3)*math.pi*(r**3)
 

r = float(input("Entrez le rayon:"))
volume = volume_sphere(r)
print(f"Le volume de la sphere est : {volume:.2f}")
