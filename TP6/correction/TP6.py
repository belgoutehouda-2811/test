import datetime

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


class Commande:
    def __init__(self, date_creation=None):
        if date_creation is None:
            self.date_creation = datetime.date.today()
        else:
            self.date_creation = date_creation
        self.produits = {}

    def ajouter_produit(self, produit, quantite):
        if produit.diminuer_stock(quantite):
            if produit in self.produits:
                self.produits[produit] += quantite
            else:
                self.produits[produit] = quantite
            print(f" {quantite} unité(s) de {produit.reference} ajoutée(s) à la commande.")
        else:
            print(f"Impossible d'ajouter {produit.reference} à la commande.")

    def afficher(self):
        print(f"\n Commande du {self.date_creation}")
        print("=" * 40)
        total = 0
        for produit, quantite in self.produits.items():
            sous_total = produit.prix_vente * quantite
            total += sous_total
            print(f"{produit.reference} : {quantite} x {produit.prix_vente} € = {sous_total} €")
        print(f" **Total : {total} dhs**")
        print("=" * 40)


if __name__ == "__main__":
    print(" TEST DE LA CLASSE PRODUIT")
    
    p1 = Produit("REF001", "Ordinateur portable", 600, 850)
    p2 = Produit("REF002", "Souris USB", 10, 25)
    p3 = Produit("REF003", "Clavier mécanique", 40, 70)

    p1.augmenter_stock(5)
    p2.augmenter_stock(20)
    p3.augmenter_stock(10)

    p1.afficher()
    p2.afficher()
    p3.afficher()

    p1.modifier_prix_vente(900)
    print(f"Prix de vente de {p1.reference} mis à jour : {p1.prix_vente} €")

    print(f"\nNombre total de produits créés : {Produit.get_nombre_produits()}")

    print("\n=== TEST DE LA CLASSE COMMANDE ===")

    commande1 = Commande()

    commande1.ajouter_produit(p1, 2)
    commande1.ajouter_produit(p2, 5)
    commande1.ajouter_produit(p3, 3)

    commande1.afficher()

    print("\n VÉRIFICATION DES STOCKS ")
    p1.afficher()
    p2.afficher()
    p3.afficher()

    print("\n TEST STOCK INSUFFISANT ")
    commande1.ajouter_produit(p1, 10)