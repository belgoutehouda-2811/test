class Client:
    def __init__(self, id_client, nom, telephone):
        self.id_client = id_client
        self.nom = nom
        self.telephone = telephone
class Plat:
    def __init__(self, id_plat, nom, prix):
        self.id_plat = id_plat
        self.nom = nom
        self.prix = prix
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestion_restaurant"
)

cursor = conn.cursor()
cursor.execute(
    "INSERT INTO client (nom, telephone) VALUES (%s, %s)",
    ("Ali", "0612345678")
)
conn.commit()
