#!/usr/bin/env python3
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.gestion_restaurant import GestionRestaurant
from models.client import Client
from models.plat import Plat
from models.commande import Commande
from models.facture import Facture
from utils.helpers import *


class RestaurantCLI:
    def __init__(self):
        self.gestion = GestionRestaurant()
        self.commande_active = None

    def menu_principal(self):
        while True:
            clear_screen()
            choix = menu_choix([
                "Gestion des clients",
                "Gestion des plats",
                "Gestion des commandes",
                "Gestion des tables",
                "Facturation",
                "Statistiques",
                "Quitter"
            ], "SYSTÈME DE GESTION DE RESTAURANT")

            if choix == 1:
                self.menu_clients()
            elif choix == 2:
                self.menu_plats()
            elif choix == 3:
                self.menu_commandes()
            elif choix == 4:
                self.menu_tables()
            elif choix == 5:
                self.menu_facturation()
            elif choix == 6:
                self.menu_statistiques()
            elif choix == 7:
                print("\nMerci d'avoir utilisé le système de gestion.")
                self.gestion.fermer_restaurant()
                break

    def menu_clients(self):
        while True:
            clear_screen()
            choix = menu_choix([
                "Lister tous les clients",
                "Ajouter un client",
                "Rechercher un client",
                "Modifier un client",
                "Supprimer un client",
                "Retour"
            ], "GESTION DES CLIENTS")

            if choix == 1:
                self.gestion.lister_clients()
                input("\nAppuyez sur Entrée pour continuer...")
            elif choix == 2:
                self.ajouter_client()
            elif choix == 3:
                self.rechercher_client()
            elif choix == 4:
                self.modifier_client()
            elif choix == 5:
                self.supprimer_client()
            elif choix == 6:
                break

    def ajouter_client(self):
        afficher_titre("AJOUT D'UN NOUVEAU CLIENT")
        nom = input("Nom: ")
        telephone = input("Téléphone: ")
        email = input("Email: ")
        adresse = input("Adresse: ")

        if confirmer_action():
            self.gestion.ajouter_client(nom, telephone, email, adresse)
        input("\nAppuyez sur Entrée pour continuer...")

    def rechercher_client(self):
        afficher_titre("RECHERCHE DE CLIENT")
        nom = input("Nom à rechercher: ")
        clients = Client.rechercher(nom)

        if clients:
            print("\nRésultats:")
            for client in clients:
                print(f"{client['id_client']:3} | {client['nom']:20} | {client['telephone']}")
        else:
            print("Aucun client trouvé")
        input("\nAppuyez sur Entrée pour continuer...")

    def modifier_client(self):
        client_id = saisir_entier("ID du client à modifier: ")
        client_data = Client.get_by_id(client_id)

        if not client_data:
            print("✗ Client non trouvé")
            input("\nAppuyez sur Entrée pour continuer...")
            return

        print(f"\nModification du client: {client_data['nom']}")
        nom = input(f"Nom [{client_data['nom']}]: ") or client_data['nom']
        telephone = input(f"Téléphone [{client_data['telephone']}]: ") or client_data['telephone']
        email = input(f"Email [{client_data['email']}]: ") or client_data['email']
        adresse = input(f"Adresse [{client_data['adresse']}]: ") or client_data['adresse']

        if confirmer_action():
            client = Client(id_client=client_id, nom=nom, telephone=telephone,
                            email=email, adresse=adresse)
            client.sauvegarder()
            print("✓ Client modifié")
        input("\nAppuyez sur Entrée pour continuer...")

    def supprimer_client(self):
        client_id = saisir_entier("ID du client à supprimer: ")

        if confirmer_action("Êtes-vous sûr de vouloir supprimer ce client? (O/N): "):
            client = Client(id_client=client_id)
            client.supprimer()
            print("✓ Client supprimé")
        input("\nAppuyez sur Entrée pour continuer...")

    def menu_plats(self):
        while True:
            clear_screen()
            choix = menu_choix([
                "Voir le menu",
                "Ajouter un plat",
                "Modifier un plat",
                "Changer disponibilité",
                "Retour"
            ], "GESTION DES PLATS")

            if choix == 1:
                self.gestion.menu_du_jour()
                input("\nAppuyez sur Entrée pour continuer...")
            elif choix == 2:
                self.ajouter_plat()
            elif choix == 3:
                self.modifier_plat()
            elif choix == 4:
                self.changer_dispo_plat()
            elif choix == 5:
                break

    def ajouter_plat(self):
        afficher_titre("AJOUT D'UN NOUVEAU PLAT")
        nom = input("Nom du plat: ")
        description = input("Description: ")
        prix = saisir_decimal("Prix (€): ", 0)

        print("\nCatégories: entrée, plat, dessert, boisson")
        categorie = input("Catégorie: ")
        temps = saisir_entier("Temps de préparation (min): ", 0)

        if confirmer_action():
            self.gestion.ajouter_plat(nom, description, prix, categorie, temps)
        input("\nAppuyez sur Entrée pour continuer...")

    def menu_commandes(self):
        while True:
            clear_screen()
            choix = menu_choix([
                "Voir commandes en cours",
                "Créer une nouvelle commande",
                "Ajouter plat à commande",
                "Voir détail commande",
                "Changer statut commande",
                "Retour"
            ], "GESTION DES COMMANDES")

            if choix == 1:
                self.afficher_commandes_en_cours()
            elif choix == 2:
                self.creer_commande()
            elif choix == 3:
                self.ajouter_plat_commande_menu()
            elif choix == 4:
                self.voir_detail_commande()
            elif choix == 5:
                self.changer_statut_commande()
            elif choix == 6:
                break

    def creer_commande(self):
        afficher_titre("NOUVELLE COMMANDE")

        print("\nClients existants:")
        clients = self.gestion.lister_clients()

        choix_client = input("\nID client (0 pour sans client): ")
        if choix_client != '0':
            client_id = int(choix_client)
        else:
            client_id = None

        table_id = saisir_entier("Numéro de table: ", 1)

        commande_id = self.gestion.creer_commande(client_id, table_id)
        self.commande_active = commande_id

        print(f"\nCommande #{commande_id} créée. Vous pouvez maintenant ajouter des plats.")
        input("\nAppuyez sur Entrée pour continuer...")

    def ajouter_plat_commande_menu(self):
        if not self.commande_active:
            commande_id = saisir_entier("ID de la commande: ")
        else:
            commande_id = self.commande_active

        print("\nMenu disponible:")
        plats = Plat.get_disponibles()
        for plat in plats:
            print(f"{plat['id_plat']:3} | {plat['nom']:25} | {plat['prix']:.2f}€")

        plat_id = saisir_entier("\nID du plat à ajouter: ")
        quantite = saisir_entier("Quantité: ", 1)

        self.gestion.ajouter_plat_commande(commande_id, plat_id, quantite)
        input("\nAppuyez sur Entrée pour continuer...")

    def afficher_commandes_en_cours(self):
        commandes = Commande.get_en_cours()
        afficher_titre("COMMANDES EN COURS")

        if not commandes:
            print("Aucune commande en cours")
        else:
            for cmd in commandes:
                print(f"#{cmd['id_commande']:3} | Table {cmd['numero_table']:2} | "
                      f"{cmd['client_nom'] or 'Anonyme':20} | "
                      f"{cmd['statut']:12} | {cmd['montant_total']:.2f}€")

        input("\nAppuyez sur Entrée pour continuer...")

    def voir_detail_commande(self):
        commande_id = saisir_entier("ID de la commande: ")
        self.gestion.afficher_commande(commande_id)
        input("\nAppuyez sur Entrée pour continuer...")

    def menu_facturation(self):
        while True:
            clear_screen()
            choix = menu_choix([
                "Générer une facture",
                "Voir factures du jour",
                "Chiffre d'affaires",
                "Retour"
            ], "FACTURATION")

            if choix == 1:
                self.generer_facture()
            elif choix == 2:
                self.voir_factures_jour()
            elif choix == 3:
                self.chiffre_affaires()
            elif choix == 4:
                break

    def generer_facture(self):
        commande_id = saisir_entier("ID de la commande à facturer: ")
        commande = Commande.get_by_id(commande_id)

        if not commande:
            print("✗ Commande non trouvée")
            input("\nAppuyez sur Entrée pour continuer...")
            return

        if commande['statut'] == 'payée':
            print("✗ Cette commande est déjà payée")
            input("\nAppuyez sur Entrée pour continuer...")
            return

        self.gestion.afficher_commande(commande_id)

        print("\nMéthodes de paiement: espèces, carte, chèque")
        methode = input("Méthode de paiement: ")

        if confirmer_action("Générer la facture? (O/N): "):
            facture = Facture(id_commande=commande_id, methode_paiement=methode)
            if facture.generer():
                print(f"✓ Facture générée #{facture.id_facture}")
                print(f"Montant TTC: {facture.montant_ttc:.2f}€")
            else:
                print("✗ Erreur lors de la génération de la facture")

        input("\nAppuyez sur Entrée pour continuer...")

    def menu_tables(self):
        afficher_titre("GESTION DES TABLES")

        query = """
        SELECT t.*, e.nom as serveur_nom
        FROM TableRestaurant t
        LEFT JOIN Employe e ON t.id_serveur = e.id_employe
        ORDER BY t.numero_table
        """
        tables = self.gestion.db.fetch_all(query)

        print(f"{'Table':6} | {'Capacité':10} | {'Statut':12} | {'Serveur':15}")
        print("-" * 60)
        for table in tables:
            print(f"{table['numero_table']:6} | {table['capacite']:10} | "
                  f"{table['statut']:12} | {table['serveur_nom'] or 'Non attribué':15}")

        input("\nAppuyez sur Entrée pour continuer...")

    def menu_statistiques(self):
        while True:
            clear_screen()
            choix = menu_choix([
                "Statistiques du jour",
                "Top plats du mois",
                "Clients fréquents",
                "Retour"
            ], "STATISTIQUES")

            if choix == 1:
                self.gestion.statistiques_jour()
                input("\nAppuyez sur Entrée pour continuer...")
            elif choix == 2:
                self.top_plats_mois()
            elif choix == 3:
                self.clients_frequents()
            elif choix == 4:
                break

    def top_plats_mois(self):
        query = """
        SELECT p.nom, SUM(cp.quantite) as total_vendu, SUM(cp.quantite * cp.prix_unitaire) as chiffre
        FROM Commande_Plat cp
        JOIN Plat p ON cp.id_plat = p.id_plat
        JOIN Commande c ON cp.id_commande = c.id_commande
        WHERE MONTH(c.date_commande) = MONTH(CURDATE())
        GROUP BY p.id_plat
        ORDER BY total_vendu DESC
        LIMIT 10
        """
        resultats = self.gestion.db.fetch_all(query)

        afficher_titre("TOP 10 PLATS DU MOIS")
        print(f"{'Plat':30} | {'Quantité':10} | {'Chiffre':10}")
        print("-" * 60)
        for plat in resultats:
            print(f"{plat['nom']:30} | {plat['total_vendu']:10} | {plat['chiffre']:10.2f}€")

        input("\nAppuyez sur Entrée pour continuer...")

    def clients_frequents(self):
        query = """
        SELECT c.nom, COUNT(cmd.id_commande) as nb_commandes, SUM(cmd.montant_total) as total_depense
        FROM Client c
        JOIN Commande cmd ON c.id_client = cmd.id_client
        GROUP BY c.id_client
        ORDER BY nb_commandes DESC
        LIMIT 10
        """
        clients = self.gestion.db.fetch_all(query)

        afficher_titre("TOP 10 CLIENTS")
        print(f"{'Client':25} | {'Commandes':10} | {'Dépense totale':15}")
        print("-" * 60)
        for client in clients:
            print(f"{client['nom']:25} | {client['nb_commandes']:10} | {client['total_depense']:15.2f}€")

        input("\nAppuyez sur Entrée pour continuer...")

    def changer_statut_commande(self):
        commande_id = saisir_entier("ID de la commande: ")

        print("\nStatuts disponibles:")
        statuts = ['en attente', 'en cours', 'terminée', 'payée']
        for i, statut in enumerate(statuts, 1):
            print(f"{i}. {statut}")

        choix = saisir_entier("Nouveau statut: ", 1, 4)
        nouveau_statut = statuts[choix - 1]

        if confirmer_action():
            commande = Commande(id_commande=commande_id)
            commande.changer_statut(nouveau_statut)
            print(f"✓ Statut changé à: {nouveau_statut}")

        input("\nAppuyez sur Entrée pour continuer...")


def main():
    print("Initialisation du système de gestion de restaurant...")
    try:
        app = RestaurantCLI()
        app.menu_principal()
    except KeyboardInterrupt:
        print("\n\nProgramme interrompu. Au revoir!")
    except Exception as e:
        print(f"\nUne erreur est survenue: {e}")
        input("Appuyez sur Entrée pour quitter...")


if __name__ == "__main__":
    main()