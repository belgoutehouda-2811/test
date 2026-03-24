from database.connection import DatabaseConnection
from datetime import datetime


class Facture:
    def __init__(self, id_facture=None, id_commande=None, date_facture=None,
                 montant_ht=None, tva=None, montant_ttc=None, methode_paiement=None):
        self.id_facture = id_facture
        self.id_commande = id_commande
        self.date_facture = date_facture or datetime.now()
        self.montant_ht = montant_ht
        self.tva = tva or (montant_ht * 0.10 if montant_ht else 0)
        self.montant_ttc = montant_ttc or (montant_ht + self.tva if montant_ht else 0)
        self.methode_paiement = methode_paiement
        self.db = DatabaseConnection()

    def generer(self):
        commande_data = Commande.get_by_id(self.id_commande)
        if not commande_data:
            return False

        self.montant_ht = commande_data['montant_total']
        self.tva = self.montant_ht * 0.10
        self.montant_ttc = self.montant_ht + self.tva

        query = """
        INSERT INTO Facture (id_commande, date_facture, montant_ht, tva, montant_ttc, methode_paiement)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (self.id_commande, self.date_facture, self.montant_ht,
                  self.tva, self.montant_ttc, self.methode_paiement)

        cursor = self.db.execute_query(query, params)
        if cursor:
            self.id_facture = cursor.lastrowid

            commande = Commande(id_commande=self.id_commande)
            commande.changer_statut('payée')

            return True
        return False

    @staticmethod
    def get_by_commande(commande_id):
        db = DatabaseConnection()
        query = "SELECT * FROM Facture WHERE id_commande = %s"
        return db.fetch_one(query, (commande_id,))

    @staticmethod
    def get_chiffre_affaires(date_debut, date_fin):
        db = DatabaseConnection()
        query = """
        SELECT DATE(date_facture) as date, SUM(montant_ttc) as total
        FROM Facture
        WHERE date_facture BETWEEN %s AND %s
        GROUP BY DATE(date_facture)
        ORDER BY date
        """
        return db.fetch_all(query, (date_debut, date_fin))