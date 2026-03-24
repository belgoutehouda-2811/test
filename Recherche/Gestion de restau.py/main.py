import sys
import os
import mysql.connector
from config import DB_CONFIG


# --- 1. FONCTIONS UTILITAIRES ---

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def afficher_titre(titre):
    print("\n" + "=" * 40)
    print(f"   {titre}")
    print("=" * 40 + "\n")


def saisir_entier(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(">> Erreur : Veuillez entrer un nombre entier.")


def saisir_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(">> Erreur : Veuillez entrer un nombre décimal (ex: 12.5).")


# --- 2. GESTION BASE DE DONNÉES ---

def get_db_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as err:
        print(f"Erreur de connexion : {err}")
        return None


# --- 3. MENU PRINCIPAL CLI ---

class RestaurantCLI:
    def menu_principal(self):
        while True:
            clear_screen()
            afficher_titre("RESTAURANT - MENU PRINCIPAL")
            print("1. Gestion des Clients")
            print("2. Gestion des Plats (Menu)")
            print("3. Prise de Commande")
            print("4. Quitter")

            choix = input("\nVotre choix : ")

            if choix == '1':
                self.menu_clients()
            elif choix == '2':
                self.menu_plats()
            elif choix == '3':
                self.menu_commandes()
            elif choix == '4':
                print("Au revoir !")
                break
            else:
                input("Choix invalide. Appuyez sur Entrée...")

    # --- GESTION CLIENTS ---
    def menu_clients(self):
        while True:
            clear_screen()
            afficher_titre("GESTION CLIENTS")
            print("1. Lister les clients")
            print("2. Ajouter un client")
            print("3. Retour")

            choix = input("\nChoix : ")

            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            if choix == '1':
                cursor.execute("SELECT * FROM clients")
                clients = cursor.fetchall()
                print(f"\n{'ID':<5} | {'Nom':<20} | {'Téléphone':<15}")
                print("-" * 45)
                for c in clients:
                    print(f"{c['id_client']:<5} | {c['nom']:<20} | {c['telephone']:<15}")
                input("\nAppuyez sur Entrée...")

            elif choix == '2':
                nom = input("Nom : ")
                tel = input("Téléphone : ")
                email = input("Email : ")
                cursor.execute("INSERT INTO clients (nom, telephone, email) VALUES (%s, %s, %s)", (nom, tel, email))
                conn.commit()
                print("✅ Client ajouté !")
                input("\nAppuyez sur Entrée...")

            elif choix == '3':
                conn.close()
                break

            if conn.is_connected():
                conn.close()

    # --- GESTION PLATS ---
    def menu_plats(self):
        while True:
            clear_screen()
            afficher_titre("GESTION PLATS")
            print("1. Voir le Menu")
            print("2. Ajouter un Plat")
            print("3. Retour")

            choix = input("\nChoix : ")
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            if choix == '1':
                cursor.execute("SELECT * FROM plats")
                plats = cursor.fetchall()
                print(f"\n{'ID':<5} | {'Nom':<25} | {'Prix':<10} | {'Catégorie'}")
                print("-" * 60)
                for p in plats:
                    print(f"{p['id_plat']:<5} | {p['nom']:<25} | {p['prix']:<10} | {p['categorie']}")
                input("\nAppuyez sur Entrée...")

            elif choix == '2':
                nom = input("Nom du plat : ")
                prix = saisir_float("Prix : ")
                cat = input("Catégorie (Entrée/Plat/Dessert) : ")
                desc = input("Description : ")
                cursor.execute("INSERT INTO plats (nom, prix, categorie, description) VALUES (%s, %s, %s, %s)",
                               (nom, prix, cat, desc))
                conn.commit()
                print("✅ Plat ajouté au menu !")
                input("\nAppuyez sur Entrée...")

            elif choix == '3':
                conn.close()
                break

            if conn.is_connected():
                conn.close()

    # --- GESTION COMMANDES ---
    def menu_commandes(self):
        while True:
            clear_screen()
            afficher_titre("GESTION COMMANDES")
            print("1. Voir les commandes en cours")
            print("2. Nouvelle Commande (Table)")
            print("3. Ajouter des plats à une commande")
            print("4. Retour")

            choix = input("\nChoix : ")
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            if choix == '1':
                # Jointure pour afficher le nom du client au lieu de l'ID
                sql = """
                SELECT c.id_commande, cl.nom, c.table_num, c.total, c.statut 
                FROM commandes c
                LEFT JOIN clients cl ON c.id_client = cl.id_client
                ORDER BY c.date_creation DESC
                """
                cursor.execute(sql)
                cmds = cursor.fetchall()
                print(f"\n{'ID':<5} | {'Table':<6} | {'Client':<20} | {'Total (€)':<10} | {'Statut'}")
                print("-" * 65)
                for c in cmds:
                    nom_client = c['nom'] if c['nom'] else "Inconnu"
                    print(
                        f"{c['id_commande']:<5} | {c['table_num']:<6} | {nom_client:<20} | {c['total']:<10} | {c['statut']}")
                input("\nAppuyez sur Entrée...")

            elif choix == '2':
                # Lister clients pour choisir
                cursor.execute("SELECT id_client, nom FROM clients")
                for c in cursor.fetchall():
                    print(f"{c['id_client']} - {c['nom']}")

                id_client = saisir_entier("\nID du Client : ")
                table = saisir_entier("Numéro de Table : ")

                cursor.execute(
                    "INSERT INTO commandes (id_client, table_num, total, statut) VALUES (%s, %s, 0, 'en attente')",
                    (id_client, table))
                conn.commit()
                print(f"✅ Commande créée pour la table {table} !")
                input("\nAppuyez sur Entrée...")

            elif choix == '3':
                id_cmd = saisir_entier("ID de la commande : ")

                # Afficher le menu pour choisir
                cursor.execute("SELECT id_plat, nom, prix FROM plats")
                print("\n--- MENU ---")
                plats_dict = {}
                for p in cursor.fetchall():
                    print(f"{p['id_plat']} - {p['nom']} ({p['prix']}€)")
                    plats_dict[p['id_plat']] = p['prix']

                id_plat = saisir_entier("\nID du Plat à ajouter : ")

                if id_plat in plats_dict:
                    qte = saisir_entier("Quantité : ")
                    prix_unitaire = plats_dict[id_plat]

                    # 1. Ajouter dans commande_plats
                    cursor.execute("INSERT INTO commande_plats (id_commande, id_plat, quantite) VALUES (%s, %s, %s)",
                                   (id_cmd, id_plat, qte))

                    # 2. Mettre à jour le total
                    total_add = float(prix_unitaire) * qte
                    cursor.execute("UPDATE commandes SET total = total + %s WHERE id_commande = %s",
                                   (total_add, id_cmd))

                    conn.commit()
                    print("✅ Plat ajouté !")
                else:
                    print("❌ ID Plat incorrect.")
                input("\nAppuyez sur Entrée...")

            elif choix == '4':
                conn.close()
                break

            if conn.is_connected():
                conn.close()


if __name__ == "__main__":
    app = RestaurantCLI()
    app.menu_principal()