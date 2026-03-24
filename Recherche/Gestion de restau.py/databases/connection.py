import mysql.connector
from mysql.connector import Error
import os


class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',  # Laisser vide par défaut
                database='restaurant_db',
                port=3306
            )
            print("✓ Connexion à la base de données établie")
            return self.connection
        except Error as e:
            print(f"✗ Erreur de connexion: {e}")
            return None

    def get_cursor(self):
        if self.connection is None:
            self.connect()
        return self.connection.cursor(dictionary=True)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("✓ Connexion fermée")

    def execute_query(self, query, params=None):
        cursor = self.get_cursor()
        try:
            cursor.execute(query, params or ())
            self.connection.commit()
            return cursor
        except Error as e:
            print(f"✗ Erreur d'exécution: {e}")
            return None

    def fetch_all(self, query, params=None):
        cursor = self.execute_query(query, params)
        if cursor:
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def fetch_one(self, query, params=None):
        cursor = self.execute_query(query, params)
        if cursor:
            result = cursor.fetchone()
            cursor.close()
            return result
        return None