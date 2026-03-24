from datetime import datetime

class Produit:
    nb_produits = 0

    def __init__(self, reference, designation, prix_achat, prix_vente):
        self.reference = reference
        self.designation = designation
        self.prix_achat = prix_achat
        self.prix_vente = prix_vente
        self.stock = 0
        Produit.nb_produits += 1

    def afficher(self):
        print(f"Ref: {self.reference}, Désignation: {self.designation}, "
              f"Achat: {self.prix_achat}, Vente: {self.prix_vente}, Stock: {self.stock}")

    def modifier_prix(self, prix_achat, prix_vente):
        self.prix_achat = prix_achat
        self.prix_vente = prix_vente

    def ajouter_stock(self, qte):
        self.stock += qte

    def retirer_stock(self, qte):
        if qte <= self.stock:
            self.stock -= qte
        else:
            print("Stock insuffisant !")

    classmethod
    def get_nb_produits(cls):
        return cls.nb_produits


class Commande:
    def __init__(self):
        self.date = datetime.now()
        self.produits = {}

    def ajouter_produit(self, produit, qte):
        if produit.stock >= qte:
            self.produits[produit] = qte
        else:
            print("Stock insuffisant pour ce produit.")

    def afficher_commande(self):
        print(f"Commande du {self.date}")
        for produit, qte in self.produits.items():
            print(f"{produit.designation} - {qte} unités")

    def valider(self):
        for produit, qte in self.produits.items():
            produit.retirer_stock(qte)
        print("Commande validée et stock mis à jour.")  