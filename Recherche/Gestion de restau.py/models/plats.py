from database.connection import DatabaseConnection


class Plat:
    def __init__(self, id_plat=None, nom=None, description=None, prix=None,
                 categorie=None, disponible=True, temps_preparation=None):
        self.id_plat = id_plat
        self.nom = nom
        self.description = description
        self.prix = prix
        self.categorie = categorie
        self.disponible = disponible
        self.temps_preparation = temps_preparation
        self.db = DatabaseConnection()

    def sauvegarder(self):
        if self.id_plat:
            query = """
            UPDATE Plat 
            SET nom = %s, description = %s, prix = %s, categorie = %s, 
                disponible = %s, temps_preparation = %s
            WHERE id_plat = %s
            """
            params = (self.nom, self.description, self.prix, self.categorie,
                      self.disponible, self.temps_preparation, self.id_plat)
        else:
            query = """
            INSERT INTO Plat (nom, description, prix, categorie, disponible, temps_preparation)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            params = (self.nom, self.description, self.prix, self.categorie,
                      self.disponible, self.temps_preparation)

        cursor = self.db.execute_query(query, params)
        if cursor and not self.id_plat:
            self.id_plat = cursor.lastrowid
        return self.id_plat

    @staticmethod
    def get_all():
        db = DatabaseConnection()
        query = "SELECT * FROM Plat ORDER BY categorie, nom"
        return db.fetch_all(query)

    @staticmethod
    def get_disponibles():
        db = DatabaseConnection()
        query = "SELECT * FROM Plat WHERE disponible = TRUE ORDER BY categorie, nom"
        return db.fetch_all(query)

    @staticmethod
    def get_by_categorie(categorie):
        db = DatabaseConnection()
        query = "SELECT * FROM Plat WHERE categorie = %s AND disponible = TRUE"
        return db.fetch_all(query, (categorie,))

    @staticmethod
    def get_by_id(plat_id):
        db = DatabaseConnection()
        query = "SELECT * FROM Plat WHERE id_plat = %s"
        return db.fetch_one(query, (plat_id,))

    def afficher(self):
        print(f"\nID: {self.id_plat}")
        print(f"Nom: {self.nom}")
        print(f"Description: {self.description}")
        print(f"Prix: {self.prix}€")
        print(f"Catégorie: {self.categorie}")
        print(f"Disponible: {'Oui' if self.disponible else 'Non'}")
        print(f"Temps préparation: {self.temps_preparation} min")