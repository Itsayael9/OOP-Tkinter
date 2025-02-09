import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("Exemple de Tableau avec Tkinter")
app.geometry("500x300")

tableau = ttk.Treeview(app, columns=("Nom", "Âge", "Ville"), show="headings")

# Définir les en-têtes des colonnes
tableau.heading("Nom", text="Nom")
tableau.heading("Âge", text="Âge")
tableau.heading("Ville", text="Ville")

# Définir les tailles des colonnes
tableau.column("Nom", width=150)
tableau.column("Âge", width=100)
tableau.column("Ville", width=150)

# Ajouter des données au tableau
data = [
    ("Aya", 25, "Tanger"),
    ("Amal ", 30, "Rabat"),
    ("Sara", 22, "Tanger"),
    ("Omar", 28, "Fès"),
    ("Zineb", 26, "Marrakech"),
]

for row in data:
    tableau.insert("", tk.END, values=row)

# Afficher le tableau
tableau.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Lancer l'application
app.mainloop()
