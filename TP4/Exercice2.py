#Exercice 2 : (choix multiple)
#Proposer un programme qui permet de saisir une lettre.
#  Si la lettre est 'a', afficher "groupe A":
#  si la lettre est 'b', afficher "groupe B", si la lettre est 'c' afficher "groupe C",
#  dans tous les autres cas, afficher "Ce groupe n'existe pas".

r = input("Saisir la lettre:")
if r == "a":
 print("groupe A")
elif r == "b":
 print("groupe B")
elif r == "c":
 print("groupe C")
else:
  print("Ce groupe n'existe pas")