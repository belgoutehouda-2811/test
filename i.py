def ComparerVitesse(moto, velo):
    print(f"Vitesse de la moto ({moto.modele}): {moto.vitesse} km/h")
    print(f"Vitesse du vélo ({velo.type_velo}): environ 25 km/h")  # valeur moyenne
    if moto.vitesse > 25:
        print("La moto est plus rapide que le vélo.")
    else:
        print("Le vélo est plus rapide que cette moto.")


 # Classe fille Velo
class Velo(Vehicule):
    def __init__(self, code, prix, marque, couleur, capacite, type_velo, vitesse_moyenne):
        super().__init__(code, prix, marque, couleur, capacite)
        self.type_velo = type_velo
        self.vitesse_moyenne = vitesse_moyenne  # en km/h

    def AfficherInfos(self):
        super().AfficherInfos()
        print(f"Type de vélo: {self.type_velo}")
        print(f"Vitesse moyenne: {self.vitesse_moyenne} km/h")

    def Pedaler(self):
        print(f"Le vélo {self.marque} ({self.type_velo}) pédale à environ {self.vitesse_moyenne} km/h.")

    def Arreter(self):
        print(f"Le vélo {self.marque} s'arrête.")