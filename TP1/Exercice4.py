#Proposer un programme qui permet d’échanger les valeurs des deux variables a, b.
#1- Méthode 1 : utiliser une variable d’aide
#2- Méthode 2 : sans variable d’aide

#Méthode1 
a = input("entrez la 1 ere variable")
b = input("entrez la 2 ere variable")

c = a
a = b
b = c

print(b)

#Méthode2
a = input("entrez la 1 ere variable")
b = input("entrez la 2 ere variable")

a, b = b, a
print("a=","b=")