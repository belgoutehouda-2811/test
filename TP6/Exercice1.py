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