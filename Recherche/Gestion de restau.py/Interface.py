import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from config import DB_CONFIG


# --- Classes Modèles ---

class Database:
    @staticmethod
    def get_connection():
        try:
            return mysql.connector.connect(**DB_CONFIG)
        except mysql.connector.Error as err:
            messagebox.showerror("Erreur Base de Données", f"Impossible de se connecter : {err}")
            return None


class Plat:
    def __init__(self, nom, prix, categorie, description, id_plat=None):
        self.id_plat = id_plat
        self.nom = nom
        self.prix = prix
        self.categorie = categorie
        self.description = description

    def sauvegarder(self):
        conn = Database.get_connection()
        if conn:
            cursor = conn.cursor()
            sql = "INSERT INTO plats (nom, prix, categorie, description) VALUES (%s, %s, %s, %s)"
            valeurs = (self.nom, self.prix, self.categorie, self.description)
            try:
                cursor.execute(sql, valeurs)
                conn.commit()
                messagebox.showinfo("Succès", "Plat ajouté !")
            except mysql.connector.Error as err:
                messagebox.showerror("Erreur", f"Erreur SQL : {err}")
            finally:
                conn.close()

    @staticmethod
    def get_all():
        plats = []
        conn = Database.get_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM plats")
            results = cursor.fetchall()
            for row in results:
                plats.append(Plat(row['nom'], row['prix'], row['categorie'], row['description'], row['id_plat']))
            conn.close()
        return plats

    @staticmethod
    def get_by_id(id_plat):
        conn = Database.get_connection()
        plat = None
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM plats WHERE id_plat=%s", (id_plat,))
            row = cursor.fetchone()
            if row:
                plat = Plat(row['nom'], row['prix'], row['categorie'], row['description'], row['id_plat'])
            conn.close()
        return plat


class Client:
    def __init__(self, nom, telephone, email, id_client=None):
        self.id_client = id_client
        self.nom = nom
        self.telephone = telephone
        self.email = email

    def sauvegarder(self):
        conn = Database.get_connection()
        if conn:
            cursor = conn.cursor()
            sql = "INSERT INTO clients (nom, telephone, email) VALUES (%s, %s, %s)"
            valeurs = (self.nom, self.telephone, self.email)
            try:
                cursor.execute(sql, valeurs)
                conn.commit()
                messagebox.showinfo("Succès", "Client ajouté !")
            except mysql.connector.Error as err:
                messagebox.showerror("Erreur", f"Erreur SQL : {err}")
            finally:
                conn.close()

    @staticmethod
    def get_all():
        clients = []
        conn = Database.get_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM clients")
            results = cursor.fetchall()
            for row in results:
                clients.append(Client(row['nom'], row['telephone'], row['email'], row['id_client']))
            conn.close()
        return clients

    @staticmethod
    def get_by_id(client_id):
        conn = Database.get_connection()
        client = None
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM clients WHERE id_client = %s", (client_id,))
            row = cursor.fetchone()
            if row:
                client = Client(row['nom'], row['telephone'], row['email'], row['id_client'])
            conn.close()
        return client


class Commande:
    def __init__(self, id_client, table, total=0, statut="en attente", id_commande=None):
        self.id_commande = id_commande
        self.id_client = id_client
        self.table = table
        self.total = total
        self.statut = statut

    def sauvegarder(self):
        conn = Database.get_connection()
        if conn:
            cursor = conn.cursor()
            sql = "INSERT INTO commandes (id_client, table_num, total, statut) VALUES (%s, %s, %s, %s)"
            valeurs = (self.id_client, self.table, self.total, self.statut)
            try:
                cursor.execute(sql, valeurs)
                conn.commit()
                messagebox.showinfo("Succès", "Commande créée !")
            except mysql.connector.Error as err:
                messagebox.showerror("Erreur", f"Erreur commande : {err}")
            finally:
                conn.close()

    @staticmethod
    def ajouter_plat(id_commande, id_plat, quantite, prix_unitaire):
        conn = Database.get_connection()
        if conn:
            cursor = conn.cursor()
            try:
                # 1. Ajouter le détail
                sql_insert = "INSERT INTO commande_plats (id_commande, id_plat, quantite) VALUES (%s, %s, %s)"
                cursor.execute(sql_insert, (id_commande, id_plat, quantite))

                # 2. Mettre à jour le total de la commande
                nouveau_total = float(quantite) * float(prix_unitaire)
                sql_update = "UPDATE commandes SET total = total + %s WHERE id_commande = %s"
                cursor.execute(sql_update, (nouveau_total, id_commande))

                conn.commit()
                messagebox.showinfo("Succès", "Plat ajouté à la commande !")
            except mysql.connector.Error as err:
                messagebox.showerror("Erreur", f"Erreur lors de l'ajout : {err}")
            finally:
                conn.close()

    @staticmethod
    def get_details(id_commande):
        details = []
        conn = Database.get_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            # Jointure pour récupérer le nom du plat et le prix
            sql = """
                SELECT p.nom, p.prix, cp.quantite 
                FROM commande_plats cp
                JOIN plats p ON cp.id_plat = p.id_plat
                WHERE cp.id_commande = %s
            """
            cursor.execute(sql, (id_commande,))
            details = cursor.fetchall()
            conn.close()
        return details

    @staticmethod
    def get_all():
        commandes = []
        conn = Database.get_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM commandes ORDER BY date_creation DESC")
            results = cursor.fetchall()
            for row in results:
                commandes.append(
                    Commande(row['id_client'], row['table_num'], row['total'], row['statut'], row['id_commande']))
            conn.close()
        return commandes


# --- Interface Graphique ---

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Système de Gestion Restaurant")
        self.root.geometry("1100x650")

        style = ttk.Style()
        style.theme_use('clam')

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        self.setup_plats_tab()
        self.setup_clients_tab()
        self.setup_commandes_tab()

    def setup_plats_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Gestion des Plats")

        left_frame = ttk.LabelFrame(frame, text="Nouveau Plat", padding=10)
        left_frame.pack(side='left', fill='y', padx=10, pady=10)

        ttk.Label(left_frame, text="Nom du plat:").pack(anchor='w')
        self.entry_nom_plat = ttk.Entry(left_frame)
        self.entry_nom_plat.pack(fill='x', pady=5)

        ttk.Label(left_frame, text="Prix (€):").pack(anchor='w')
        self.entry_prix_plat = ttk.Entry(left_frame)
        self.entry_prix_plat.pack(fill='x', pady=5)

        ttk.Label(left_frame, text="Catégorie:").pack(anchor='w')
        self.combo_cat = ttk.Combobox(left_frame, values=["Entrée", "Plat", "Dessert", "Boisson"])
        self.combo_cat.pack(fill='x', pady=5)

        ttk.Label(left_frame, text="Description:").pack(anchor='w')
        self.entry_desc_plat = ttk.Entry(left_frame)
        self.entry_desc_plat.pack(fill='x', pady=5)

        ttk.Button(left_frame, text="Ajouter Plat", command=self.ajouter_plat).pack(pady=20, fill='x')

        cols = ('ID', 'Nom', 'Prix', 'Catégorie', 'Description')
        self.tree_plats = ttk.Treeview(frame, columns=cols, show='headings')
        for col in cols:
            self.tree_plats.heading(col, text=col)
            self.tree_plats.column(col, width=100)

        self.tree_plats.pack(side='right', fill='both', expand=True, padx=10, pady=10)
        self.actualiser_liste_plats()

    def setup_clients_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Gestion Clients")

        left_frame = ttk.LabelFrame(frame, text="Nouveau Client", padding=10)
        left_frame.pack(side='left', fill='y', padx=10, pady=10)

        ttk.Label(left_frame, text="Nom:").pack(anchor='w')
        self.entry_nom_client = ttk.Entry(left_frame)
        self.entry_nom_client.pack(fill='x', pady=5)

        ttk.Label(left_frame, text="Téléphone:").pack(anchor='w')
        self.entry_tel_client = ttk.Entry(left_frame)
        self.entry_tel_client.pack(fill='x', pady=5)

        ttk.Label(left_frame, text="Email:").pack(anchor='w')
        self.entry_email_client = ttk.Entry(left_frame)
        self.entry_email_client.pack(fill='x', pady=5)

        ttk.Button(left_frame, text="Ajouter Client", command=self.ajouter_client).pack(pady=20, fill='x')

        cols = ('ID', 'Nom', 'Téléphone', 'Email')
        self.tree_clients = ttk.Treeview(frame, columns=cols, show='headings')
        for col in cols:
            self.tree_clients.heading(col, text=col)
        self.tree_clients.pack(side='right', fill='both', expand=True, padx=10, pady=10)
        self.actualiser_liste_clients()

    def setup_commandes_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Prise de Commande")

        # --- Partie HAUT : Création & Ajout ---
        top_container = ttk.Frame(frame)
        top_container.pack(fill='x', padx=10, pady=10)

        # 1. Nouvelle Commande (Gauche)
        grp_new = ttk.LabelFrame(top_container, text="1. Nouvelle Table", padding=10)
        grp_new.pack(side='left', fill='both', expand=True, padx=5)

        ttk.Label(grp_new, text="Client:").grid(row=0, column=0, sticky='w')
        self.combo_client = ttk.Combobox(grp_new, width=20)
        self.combo_client.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(grp_new, text="Table N°:").grid(row=1, column=0, sticky='w')
        self.entry_table = ttk.Entry(grp_new, width=10)
        self.entry_table.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(grp_new, text="Créer Commande", command=self.creer_commande).grid(row=2, column=0, columnspan=2,
                                                                                     pady=10, sticky='ew')

        # 2. Ajouter Plat au Panier (Droite)
        grp_add = ttk.LabelFrame(top_container, text="2. Ajouter plat à commande", padding=10)
        grp_add.pack(side='left', fill='both', expand=True, padx=5)

        ttk.Label(grp_add, text="Commande ID:").grid(row=0, column=0, sticky='w')
        self.entry_cmd_id = ttk.Entry(grp_add, width=10)
        self.entry_cmd_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(grp_add, text="Plat:").grid(row=1, column=0, sticky='w')
        self.combo_plats_commande = ttk.Combobox(grp_add, width=25)
        self.combo_plats_commande.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(grp_add, text="Quantité:").grid(row=2, column=0, sticky='w')
        self.entry_qte = ttk.Entry(grp_add, width=10)
        self.entry_qte.insert(0, "1")
        self.entry_qte.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(grp_add, text="Ajouter plat", command=self.ajouter_plat_commande).grid(row=3, column=0, columnspan=2,
                                                                                          pady=10, sticky='ew')

        # --- Partie BAS : Liste des Commandes ---
        self.tree_commandes = ttk.Treeview(frame, columns=('ID', 'Client', 'Table', 'Total', 'Statut'), show='headings')
        for col in ('ID', 'Client', 'Table', 'Total', 'Statut'):
            self.tree_commandes.heading(col, text=col)
            self.tree_commandes.column(col, width=100)

        self.tree_commandes.pack(fill='both', expand=True, padx=10, pady=5)

        # Bouton Voir Détails
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill='x', padx=10, pady=10)
        ttk.Button(btn_frame, text="Actualiser", command=self.actualiser_liste_commandes).pack(side='left')
        ttk.Button(btn_frame, text="Voir détail commande", command=self.voir_details_commande).pack(side='right')

        self.actualiser_combo_clients()
        self.actualiser_combo_plats()
        self.actualiser_liste_commandes()

    # --- Logique Métier ---

    def ajouter_plat(self):
        try:
            prix = float(self.entry_prix_plat.get())
            p = Plat(self.entry_nom_plat.get(), prix, self.combo_cat.get(), self.entry_desc_plat.get())
            p.sauvegarder()
            self.actualiser_liste_plats()
            self.actualiser_combo_plats()  # Mettre à jour la liste des plats dispo
        except ValueError:
            messagebox.showerror("Erreur", "Le prix doit être un nombre")

    def ajouter_client(self):
        c = Client(self.entry_nom_client.get(), self.entry_tel_client.get(), self.entry_email_client.get())
        c.sauvegarder()
        self.actualiser_liste_clients()
        self.actualiser_combo_clients()

    def creer_commande(self):
        selection = self.combo_client.get()
        if not selection:
            messagebox.showwarning("Attention", "Sélectionnez un client")
            return
        id_client = int(selection.split(' - ')[0])
        cmd = Commande(id_client, self.entry_table.get())
        cmd.sauvegarder()
        self.actualiser_liste_commandes()

    def ajouter_plat_commande(self):
        # 1. Récupérer ID Commande
        cmd_id = self.entry_cmd_id.get()
        if not cmd_id:
            messagebox.showwarning("Erreur", "Entrez l'ID de la commande")
            return

        # 2. Récupérer le Plat et son prix
        plat_selection = self.combo_plats_commande.get()
        if not plat_selection:
            messagebox.showwarning("Erreur", "Sélectionnez un plat")
            return

        # Le format est "ID - Nom - PRIX€"
        try:
            parts = plat_selection.split(' - ')
            id_plat = int(parts[0])
            prix_str = parts[2].replace('€', '')
            prix = float(prix_str)
            qte = int(self.entry_qte.get())

            # 3. Sauvegarder
            Commande.ajouter_plat(cmd_id, id_plat, qte, prix)
            self.actualiser_liste_commandes()

        except Exception as e:
            messagebox.showerror("Erreur", f"Problème de données : {e}")

    def voir_details_commande(self):
        # Récupérer la ligne sélectionnée
        selected = self.tree_commandes.selection()
        if not selected:
            # Sinon essayer de prendre l'ID tapé manuellement
            cmd_id = self.entry_cmd_id.get()
            if not cmd_id:
                messagebox.showwarning("Info", "Sélectionnez une commande dans la liste")
                return
        else:
            item = self.tree_commandes.item(selected[0])
            cmd_id = item['values'][0]

        details = Commande.get_details(cmd_id)

        # Afficher dans une popup
        popup = tk.Toplevel()
        popup.title(f"Détail Commande #{cmd_id}")
        popup.geometry("300x400")

        text = tk.Text(popup)
        text.pack(fill='both', expand=True)

        text.insert('end', f"--- Commande #{cmd_id} ---\n\n")
        total_verif = 0
        for d in details:
            sous_total = d['prix'] * d['quantite']
            total_verif += sous_total
            text.insert('end', f"- {d['quantite']}x {d['nom']} ({d['prix']}€)\n")
            text.insert('end', f"  = {sous_total:.2f}€\n\n")

        text.insert('end', "-----------------\n")
        text.insert('end', f"TOTAL: {total_verif:.2f}€")

    # --- Actualisation ---

    def actualiser_liste_plats(self):
        for item in self.tree_plats.get_children():
            self.tree_plats.delete(item)
        for p in Plat.get_all():
            self.tree_plats.insert('', 'end', values=(p.id_plat, p.nom, f"{p.prix}€", p.categorie, p.description))

    def actualiser_liste_clients(self):
        for item in self.tree_clients.get_children():
            self.tree_clients.delete(item)
        for c in Client.get_all():
            self.tree_clients.insert('', 'end', values=(c.id_client, c.nom, c.telephone, c.email))

    def actualiser_liste_commandes(self):
        for item in self.tree_commandes.get_children():
            self.tree_commandes.delete(item)
        for cmd in Commande.get_all():
            nom_client = "Inconnu"
            client = Client.get_by_id(cmd.id_client)
            if client:
                nom_client = client.nom
            self.tree_commandes.insert('', 'end',
                                       values=(cmd.id_commande, nom_client, cmd.table, f"{cmd.total}€", cmd.statut))

    def actualiser_combo_clients(self):
        vals = [f"{c.id_client} - {c.nom}" for c in Client.get_all()]
        self.combo_client['values'] = vals

    def actualiser_combo_plats(self):
        # On affiche "ID - Nom - Prix" pour faciliter le calcul
        vals = [f"{p.id_plat} - {p.nom} - {p.prix}€" for p in Plat.get_all()]
        self.combo_plats_commande['values'] = vals


if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()