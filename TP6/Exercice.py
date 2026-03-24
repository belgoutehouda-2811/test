#

class Produit:
    def _init_(self,nom,prix,qte):
        self.nom = nom
        self,prix =prix
        self.qte= qte

    def afficher_produit(self):
        print(f"{self.nom} - {self.prix}dh - {self.qte}unités")

class Commande : 
    def _init_(self,num,liste_produites,montant):
        self.num = num
        self.liste_produites = []
        self.montant = 0

    def ajouter_produit(self,p):
        self.liste_produits.append(p)

    def calculer_total(self):
        self.montant=sum(p.prix*p.qte for p in self.liste_produits)

    def afficher_commande(self):
        print(f"Commande n{self.num}")
        for p in self.liste_produits:
            p.afficher_produit()
        print(f"Montant total : {self.montant}dh")