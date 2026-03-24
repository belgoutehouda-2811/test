from database.connection import DatabaseConnection
from datetime import datetime


class Commande:
    def __init__(self, id_commande=None, id_client=None, id_table=None,
                 date_commande=None, statut='en attente', montant_total=0):
        self.id_commande = id_commande
        self.id_client = id_client
        self.id_table = id_table
        self.date_commande = date_commande or datetime.now()
        self.statut = statut
        self.montant_total = montant_total
        self.db = DatabaseConnection()
        self.plats = []

    def sauvegarder(self):
        if self.id_commande:
            query = """
            UPDATE Commande 
            SET id_client = %s, id_table = %s, statut = %s, montant_total = %s
            WHERE id_commande = %s
            """
            params = (self.id_client, self.id_table, self.statut,
                      self.montant_total, self.id_commande)
        else:
            query = """
            INSERT INTO Commande (id_client, id_table, date_commande, statut, montant_total)
            VALUES (%s, %s, %s, %s, %s)
            """
            params = (self.id_client, self.id_table, self.date_commande,
                      self.statut, self.montant_total)

        cursor = self.db.execute_query(query, params)
        if cursor and not self.id_commande:
            self.id_commande = cursor.lastrowid
        return self.id_commande

    def ajouter_plat(self, plat_id, quantite, prix_unitaire):
        query = """
        INSERT INTO Commande_Plat (id_commande, id_plat, quantite, prix_unitaire)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE quantite = quantite + VALUES(quantite)
        """
        self.db.execute_query(query, (self.id_commande, plat_id, quantite, prix_unitaire))
        self.plats.append({'id_plat': plat_id, 'quantite': quantite})

    def get_plats(self):
        query = """
        SELECT p.nom, cp.quantite, cp.prix_unitaire, 
               (cp.quantite * cp.prix_unitaire) as total
        FROM Commande_Plat cp
        JOIN Plat p ON cp.id_plat = p.id_plat
        WHERE cp.id_commande = %s
        """
        return self.db.fetch_all(query, (self.id_commande,))

    def calculer_total(self):
        query = """
        SELECT SUM(quantite * prix_unitaire) as total
        FROM Commande_Plat
        WHERE id_commande = %s
        """
        result = self.db.fetch_one(query, (self.id_commande,))
        self.montant_total = result['total'] if result and result['total'] else 0
        return self.montant_total

    def changer_statut(self, nouveau_statut):
        self.statut = nouveau_statut
        self.sauvegarder()

    @staticmethod
    def get_all():
        db = DatabaseConnection()
        query = """
        SELECT c.*, cl.nom as client_nom, t.numero_table
        FROM Commande c
        LEFT JOIN Client cl ON c.id_client = cl.id_client
        JOIN TableRestaurant t ON c.id_table = t.id_table
        ORDER BY c.date_commande DESC
        """
        return db.fetch_all(query)

    @staticmethod
    def get_by_id(commande_id):
        db = DatabaseConnection()
        query = """
        SELECT c.*, cl.nom as client_nom, cl.telephone, t.numero_table
        FROM Commande c
        LEFT JOIN Client cl ON c.id_client = cl.id_client
        JOIN TableRestaurant t ON c.id_table = t.id_table
        WHERE c.id_commande = %s
        """
        return db.fetch_one(query, (commande_id,))

    @staticmethod
    def get_en_cours():
        db = DatabaseConnection()
        query = """
        SELECT c.*, cl.nom as client_nom, t.numero_table
        FROM Commande c
        LEFT JOIN Client cl ON c.id_client = cl.id_client
        JOIN TableRestaurant t ON c.id_table = t.id_table
        WHERE c.statut IN ('en attente', 'en cours')
        ORDER BY c.date_commande
        """
        return db.fetch_all(query)