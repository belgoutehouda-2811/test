# Classe mère Vehicule
class Vehicule:
    def _init_(self, code, prix, marque, couleur, capacite):
        self.code = code
        self.prix = prix
        self.marque = marque
        self.couleur = couleur
        self.capacite = capacite
    def AfficherInfos(self):
        print(f"Code: {self.code}")
        print(f"Prix: {self.prix}")
        print(f"Marque: {self.marque}")
        print(f"Couleur: {self.couleur}")
        print(f"Capacité: {self.capacite} personnes")

# Classe fille Moto
class Moto:
    def _init_(self):
        pass

class Moto(Vehicule):
    def _init_(self, code, prix, marque, couleur, capacite, vitesse, modele):
        super()._init_(code, prix, marque, couleur, capacite)
        self.vitesse = vitesse
        self.modele = modele
    def AfficherInfos(self):
        super().AfficherInfos()
        print(f"Vitesse: {self.vitesse} km/h")
        print(f"Modèle: {self.modele}")
    def Accelerer(self):
        print(f"La moto {self.marque} accélère.")
            
    def Arreter(self):
        print(f"La moto {self.marque} s'arrête.")
    def AfficherModele(self):
        print(f"Le modèle de la moto est : {self.modele}")
# Classe fille Vélo
class Velo(Vehicule):
    pass
moto = Moto(code=101, prix=15000, marque="Yamaha", couleur="Noir", capacite=2, vitesse=180, modele="YZF-R1")
print("Informations Moto:")
moto.AfficherInfos()
moto.Accelerer()
moto.Arreter()
moto.AfficherModele()