#1. Définir l’ensemble de classes
#  à implémenter pour assurer la gestion commerciale de la société.

class Produit:
    nombre_produits = 0

    def __init__(self, reference, designation, prix_achat, prix_vente):
        self.reference = reference
        self.designation = designation
        self.prix_achat = prix_achat
        self.prix_vente = prix_vente
        self.stock = 0
        Produit.nombre_produits += 1

    @classmethod
    def get_nombre_produits(cls):
        return cls.nombre_produits

    def modifier_prix_achat(self, nouveau_prix):
        self.prix_achat = nouveau_prix

    def modifier_prix_vente(self, nouveau_prix):
        self.prix_vente = nouveau_prix

    def augmenter_stock(self, quantite):
        self.stock += quantite

    def diminuer_stock(self, quantite):
        if self.stock >= quantite:
            self.stock -= quantite
            return True
        else:
            print(f"Stock insuffisant pour {self.reference}. Stock actuel : {self.stock}")
            return False

    def afficher(self):
        print(f"Référence : {self.reference}")
        print(f"Désignation : {self.designation}")
        print(f"Prix d'achat : {self.prix_achat} €")
        print(f"Prix de vente : {self.prix_vente} €")
        print(f"Stock : {self.stock} unités")
        print("-" * 30)

