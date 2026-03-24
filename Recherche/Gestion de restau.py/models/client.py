from database.connection import DatabaseConnection


class Client:
    def __init__(self, id_client=None, nom=None, telephone=None, email=None, adresse=None):
        self.id_client = id_client
        self.nom = nom
        self.telephone = telephone
        self.email = email
        self.adresse = adresse
        self.db = DatabaseConnection()

    def sauvegarder(self):
        if self.id_client:
            query = """
            UPDATE Client 
            SET nom = %s, telephone = %s, email = %s, adresse = %s
            WHERE id_client = %s
            """
            params = (self.nom, self.telephone, self.email, self.adresse, self.id_client)
        else:
            query = """
            INSERT INTO Client (nom, telephone, email, adresse)
            VALUES (%s, %s, %s, %s)
            """
            params = (self.nom, self.telephone, self.email, self.adresse)

        cursor = self.db.execute_query(query, params)
        if cursor and not self.id_client:
            self.id_client = cursor.lastrowid
        return self.id_client

    def supprimer(self):
        query = "DELETE FROM Client WHERE id_client = %s"
        self.db.execute_query(query, (self.id_client,))

    @staticmethod
    def get_all():
        db = DatabaseConnection()
        query = "SELECT * FROM Client ORDER BY nom"
        return db.fetch_all(query)

    @staticmethod
    def get_by_id(client_id):
        db = DatabaseConnection()
        query = "SELECT * FROM Client WHERE id_client = %s"
        return db.fetch_one(query, (client_id,))

    @staticmethod
    def rechercher(nom):
        db = DatabaseConnection()
        query = "SELECT * FROM Client WHERE nom LIKE %s"
        return db.fetch_all(query, (f"%{nom}%",))

    def afficher(self):
        print(f"\nID: {self.id_client}")
        print(f"Nom: {self.nom}")
        print(f"Téléphone: {self.telephone}")
        print(f"Email: {self.email}")
        print(f"Adresse: {self.adresse}")