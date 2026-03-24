from models.client import Client
from models.plat import Plat
from models.commande import Commande
from models.facture import Facture
from database.connection import DatabaseConnection


class GestionRestaurant:
    def __init__(self):
        self.db = DatabaseConnection()
        self.db.connect()

    # Gestion des clients
    def ajouter_client(self, nom, telephone, email, adresse):
        client = Client(nom=nom, telephone=telephone, email=email, adresse=adresse)
        client_id = client.sauvegarder()
        print(f"✓ Client ajouté avec l'ID: {client_id}")
        return client_id

    def lister_clients(self):
        clients = Client.get_all()
        print("\n" + "=" * 60)
        print("LISTE DES CLIENTS")
        print("=" * 60)
        for client in clients:
            print(f"{client['id_client']:3} | {client['nom']:20} | {client['telephone']:12} | {client['email']}")
        print(f"Total: {len(clients)} clients")
        return clients

    # Gestion des plats
    def ajouter_plat(self, nom, description, prix, categorie, temps_preparation):
        plat = Plat(nom=nom, description=description, prix=prix,
                    categorie=categorie, temps_preparation=temps_preparation)
        plat_id = plat.sauvegarder()
        print(f"✓ Plat ajouté avec l'ID: {plat_id}")
        return plat_id

    def menu_du_jour(self):
        plats = Plat.get_disponibles()
        print("\n" + "=" * 60)
        print("MENU DU JOUR")
        print("=" * 60)

        categories = {}
        for plat in plats:
            if plat['categorie'] not in categories:
                categories[plat['categorie']] = []
            categories[plat['categorie']].append(plat)

        for categorie, plats_cat in categories.items():
            print(f"\n{categorie.upper()}:")
            for plat in plats_cat:
                print(
                    f"  {plat['id_plat']:3} | {plat['nom']:25} | {plat['prix']:6.2f}€ | {plat['description'][:30]}...")

        return plats

    # Gestion des commandes
    def creer_commande(self, client_id, table_id):
        commande = Commande(id_client=client_id, id_table=table_id)
        commande_id = commande.sauvegarder()
        print(f"✓ Commande créée avec l'ID: {commande_id}")
        return commande_id

    def ajouter_plat_commande(self, commande_id, plat_id, quantite):
        plat = Plat.get_by_id(plat_id)
        if not plat:
            print("✗ Plat non trouvé")
            return False

        commande = Commande(id_commande=commande_id)
        commande.ajouter_plat(plat_id, quantite, plat['prix'])
        print(f"✓ {quantite} x {plat['nom']} ajouté à la commande")
        return True

    def afficher_commande(self, commande_id):
        commande = Commande.get_by_id(commande_id)
        if not commande:
            print("✗ Commande non trouvée")
            return

        print("\n" + "=" * 60)
        print("DÉTAIL DE LA COMMANDE")
        print("=" * 60)
        print(f"Commande #{commande_id}")
        print(f"Client: {commande['client_nom'] or 'Non renseigné'}")
        print(f"Table: {commande['numero_table']}")
        print(f"Date: {commande['date_commande']}")
        print(f"Statut: {commande['statut']}")
        print("-" * 60)

        plats = Commande(id_commande=commande_id).get_plats()
        total = 0
        for plat in plats:
            ligne_total = plat['quantite'] * plat['prix_unitaire']
            total += ligne_total
            print(f"{plat['nom']:30} x{plat['quantite']:2} = {ligne_total:6.2f}€")

        print("-" * 60)
        print(f"TOTAL: {total:36.2f}€")

    # Statistiques
    def statistiques_jour(self):
        query = """
        SELECT 
            COUNT(*) as nb_commandes,
            SUM(montant_total) as chiffre_affaires,
            AVG(montant_total) as moyenne_commande
        FROM Commande
        WHERE DATE(date_commande) = CURDATE()
        """
        stats = self.db.fetch_one(query)

        print("\n" + "=" * 60)
        print("STATISTIQUES DU JOUR")
        print("=" * 60)
        print(f"Commandes aujourd'hui: {stats['nb_commandes'] or 0}")
        print(f"Chiffre d'affaires: {stats['chiffre_affaires'] or 0:.2f}€")
        print(f"Moyenne par commande: {stats['moyenne_commande'] or 0:.2f}€")

        query_plats = """
        SELECT p.nom, SUM(cp.quantite) as quantite
        FROM Commande_Plat cp
        JOIN Plat p ON cp.id_plat = p.id_plat
        JOIN Commande c ON cp.id_commande = c.id_commande
        WHERE DATE(c.date_commande) = CURDATE()
        GROUP BY p.id_plat
        ORDER BY quantite DESC
        LIMIT 5
        """
        plats_pop = self.db.fetch_all(query_plats)

        if plats_pop:
            print("\nTOP 5 DES PLATS:")
            for plat in plats_pop:
                print(f"  {plat['nom']:25} : {plat['quantite']} commandes")

    def fermer_restaurant(self):
        self.db.disconnect()