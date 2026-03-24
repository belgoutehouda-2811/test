import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='expense_tracker'
    )

def add_transaction():
    trans_type = type_var.get()
    category = category_entry.get()
    amount = amount_entry.get()
    description = desc_entry.get()
    date = date_entry.get()
    
    if not category or not amount:
        messagebox.showerror("Error", "Please fill Category and Amount!")
        return
    
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    
    try:
        db = connect_db()
        cursor = db.cursor()
        query = "INSERT INTO transactions (type, category, amount, description, date) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (trans_type, category, float(amount), description, date))
        db.commit()
        db.close()
        
        messagebox.showinfo("Success", "Transaction added!")
        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def view_transactions():
    view_window = tk.Toplevel(root)
    view_window.title("All Transactions")
    view_window.geometry("800x400")
    
    tree = ttk.Treeview(view_window, columns=('ID', 'Type', 'Category', 'Amount', 'Description', 'Date'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Type', text='Type')
    tree.heading('Category', text='Category')
    tree.heading('Amount', text='Amount')
    tree.heading('Description', text='Description')
    tree.heading('Date', text='Date')
    
    tree.column('ID', width=40)
    tree.column('Type', width=80)
    tree.column('Category', width=100)
    tree.column('Amount', width=100)
    tree.column('Description', width=200)
    tree.column('Date', width=100)
    
    tree.pack(fill=tk.BOTH, expand=True)
    
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
        rows = cursor.fetchall()
        db.close()
        
        for row in rows:
            tree.insert('', tk.END, values=row)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_summary():
    try:
        db = connect_db()
        cursor = db.cursor()
        
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='Income'")
        income = cursor.fetchone()[0] or 0
        
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='Expense'")
        expense = cursor.fetchone()[0] or 0
        
        db.close()
        
        balance = income - expense
        
        summary_text = f"Total Income: ${income:.2f}\n"
        summary_text += f"Total Expense: ${expense:.2f}\n"
        summary_text += f"Balance: ${balance:.2f}"
        
        messagebox.showinfo("Summary", summary_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_transaction():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Transaction")
    delete_window.geometry("300x150")
    
    tk.Label(delete_window, text="Enter Transaction ID:", font=("Arial", 12)).pack(pady=10)
    id_entry = tk.Entry(delete_window, font=("Arial", 12), width=20)
    id_entry.pack(pady=10)
    
    def delete():
        trans_id = id_entry.get()
        if not trans_id:
            messagebox.showerror("Error", "Please enter ID!")
            return
        
        try:
            db = connect_db()
            cursor = db.cursor()
            cursor.execute("DELETE FROM transactions WHERE id=%s", (trans_id,))
            db.commit()
            db.close()
            
            messagebox.showinfo("Success", f"Transaction {trans_id} deleted!")
            delete_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    tk.Button(delete_window, text="Delete", command=delete, bg="#ff4444", fg="white", font=("Arial", 12)).pack(pady=10)

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x550")
root.config(bg="#f0f0f0")

title = tk.Label(root, text="Expense Tracker", font=("Arial", 20, "bold"), bg="#f0f0f0")
title.pack(pady=20)

# Type selection
type_frame = tk.Frame(root, bg="#f0f0f0")
type_frame.pack(pady=10)
tk.Label(type_frame, text="Type:", font=("Arial", 12), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
type_var = tk.StringVar(value="Expense")
tk.Radiobutton(type_frame, text="Income", variable=type_var, value="Income", font=("Arial", 11), bg="#f0f0f0").pack(side=tk.LEFT)
tk.Radiobutton(type_frame, text="Expense", variable=type_var, value="Expense", font=("Arial", 11), bg="#f0f0f0").pack(side=tk.LEFT)

# Category
category_frame = tk.Frame(root, bg="#f0f0f0")
category_frame.pack(pady=10)
tk.Label(category_frame, text="Category:", font=("Arial", 12), bg="#f0f0f0", width=12, anchor='w').pack(side=tk.LEFT)
category_entry = tk.Entry(category_frame, font=("Arial", 12), width=25)
category_entry.pack(side=tk.LEFT, padx=5)

# Amount
amount_frame = tk.Frame(root, bg="#f0f0f0")
amount_frame.pack(pady=10)
tk.Label(amount_frame, text="Amount (MAD):", font=("Arial", 12), bg="#f0f0f0", width=12, anchor='w').pack(side=tk.LEFT)
amount_entry = tk.Entry(amount_frame, font=("Arial", 12), width=25)
amount_entry.pack(side=tk.LEFT, padx=5)

# Description
desc_frame = tk.Frame(root, bg="#f0f0f0")
desc_frame.pack(pady=10)
tk.Label(desc_frame, text="Description:", font=("Arial", 12), bg="#f0f0f0", width=12, anchor='w').pack(side=tk.LEFT)
desc_entry = tk.Entry(desc_frame, font=("Arial", 12), width=25)
desc_entry.pack(side=tk.LEFT, padx=5)

# Date
date_frame = tk.Frame(root, bg="#f0f0f0")
date_frame.pack(pady=10)
tk.Label(date_frame, text="Date:", font=("Arial", 12), bg="#f0f0f0", width=12, anchor='w').pack(side=tk.LEFT)
date_entry = tk.Entry(date_frame, font=("Arial", 12), width=25)
date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
date_entry.pack(side=tk.LEFT, padx=5)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

add_btn = tk.Button(button_frame, text="Add Transaction", command=add_transaction, 
                    bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), 
                    width=15, height=2)
add_btn.pack(pady=5)

view_btn = tk.Button(button_frame, text="View All", command=view_transactions, 
                     bg="#2196F3", fg="white", font=("Arial", 12, "bold"), 
                     width=15, height=2)
view_btn.pack(pady=5)

summary_btn = tk.Button(button_frame, text="Show Summary", command=show_summary, 
                        bg="#FF9800", fg="white", font=("Arial", 12, "bold"), 
                        width=15, height=2)
summary_btn.pack(pady=5)

delete_btn = tk.Button(button_frame, text="Delete Transaction", command=delete_transaction, 
                       bg="#f44336", fg="white", font=("Arial", 12, "bold"), 
                       width=15, height=2)

delete_btn.pack(pady=5)

# Run the application
root.mainloop()