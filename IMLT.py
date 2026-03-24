# Classe fille Moto
class Moto(Vehicule):
      def _init_(self, code, prix, marque, couleur, capacite, vitesse, modele):
       super(). init_(code, prix, marque, couleur, capacite)
self.vitesse = vitesse
self.modele = modele
def AfficherInfos(self):
  super().AfficherInfos()
print(f"Vitesse: {self.vitesse} km/h")
print(f"Modèle: {self.modele}")
def Accelerer(self):
 print(f"La moto {self.marque} accélère.")
def Arreter(self):
  print(f"La moto {self marque} s'arrête.")
def AfficherModele(self):
    print(f"Le modèle de la moto est : {self.modele}")

# Classe fille Vélo
class Velo(Vehicule):                        
   pass
