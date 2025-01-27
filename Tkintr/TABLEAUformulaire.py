import tkinter as tk
from tkinter import ttk 
from tkinter import Toplevel

# fct de popup ou les infos ont vons etre ajouter 
def ouvrir_popup():
   
    popup = Toplevel(fenetre)
    popup.title("Ajouter une ligne")  
    popup.geometry("300x200")
    
    # Labels et input 
    tk.Label(popup, text="Nom:").pack(pady=5)
    entry_nom = tk.Entry(popup) .pack(pady=5)


    tk.Label(popup, text="Âge:").pack(pady=5)
    entry_age = tk.Entry(popup).pack(pady=5)

    tk.Label(popup, text="Ville:").pack(pady=5)
    entry_ville = tk.Entry(popup)
    entry_ville.pack(pady=5)

    # Fonction pour ajouter les donnees
    def ajouter_ligne():
        nom = entry_nom.get()
        age = entry_age.get()
        ville = entry_ville.get()

        if nom and age and ville:  # verification des champs non vides
            try:
                age = int(age)  # Verifier que l age est un intiger 
                tree.insert("", "end", values=(nom, age, ville))
                popup.destroy()  # Fermer la popup apres ajout
            except ValueError:
                tk.Label(popup, text="age doit etre un nombre entier ", fg="red").pack()  # Correction : ajout de pack()
        else:
            tk.Label(popup, text="Tous les champs sont obligatoires.", fg="red").pack()  # Correction : ajout de pack()

    # Bouton pour valider les donnes et appele a la fct de ajouter ligne dans le tableau 
    tk.Button(popup, text="Ajouter", command=ajouter_ligne).pack(pady=10)
    
# Fonction pour supprimer 
def supprimer_donnees():
    selected_item = tree.selection() 
    if selected_item:
        tree.delete(selected_item) 

#modifier ligne :
def modifier_ligne():
    selection = tree.selection()
    if selection:
        # Recuperer la valeur a modifier 
        item = tree.item(selection)
        valeurs = item["values"]  

        # Popup pour modifier les valeurs
        popup = Toplevel(fenetre)
        popup.title("Modifier une ligne")
        popup.geometry("300x150")

        tk.Label(popup, text="Nom:").pack(pady=5)
        entry_nom = tk.Entry(popup)
        entry_nom.insert(0, valeurs[0])  # Pré-remplir avec la valeur existante
        entry_nom.pack(pady=5)

        tk.Label(popup, text="Âge:").pack(pady=5)
        entry_age = tk.Entry(popup)
        entry_age.insert(0, valeurs[1])  # Pré-remplir avec la valeur existante
        entry_age.pack(pady=5)

        tk.Label(popup, text="Ville:").pack(pady=5)
        entry_ville = tk.Entry(popup)
        entry_ville.insert(0, valeurs[2])  # Pré-remplir avec la valeur existante
        entry_ville.pack(pady=5)

        # Fonction pour appliquer les modifications
        def appliquer_modification():
            nom = entry_nom.get()
            age = entry_age.get()
            ville = entry_ville.get()

            if nom and age and ville:  # Vérifier que les champs ne sont pas vides
                try:
                    age = int(age)  # Vérifier que l'âge est un nombre
                    tree.item(selection, values=(nom, age, ville))  # Mettre à jour la ligne
                    popup.destroy()  # Fermer la popup
                except ValueError:
                    tk.Label(popup, text="Âge doit être un nombre", fg="red").pack()

        # Bouton pour appliquer les modifications
        tk.Button(popup, text="Appliquer", command=appliquer_modification).pack(pady=10)
        
#fenetre principale 
fenetre = tk.Tk()
fenetre.title("Tableaux avec ajout de ligne")

# les colones des tableau 
colonnes = ("nom", "age", "ville")
tree = ttk.Treeview(fenetre, columns=colonnes, show="headings")
tree.pack(pady=20)

# thead de tableau 
tree.heading("nom", text="Nom")
tree.heading("age", text="Âge")
tree.heading("ville", text="Ville")

# les dimensions des colonnes
tree.column("nom", width=100, anchor="center")
tree.column("age", width=50, anchor="center")
tree.column("ville", width=100, anchor="center")

# Bouton pour ouvrir la popup
tk.Button(fenetre, text="Ajouter une ligne", command=ouvrir_popup).pack(pady=20)
# Bouton principal pour supprimer les données sélectionnées
btn_supprimer = tk.Button(fenetre , text="Supprimer", command=supprimer_donnees)
btn_supprimer.pack(pady=10)
#button de modififcation 
tk.Button(fenetre,text="modifier une lign ",command=modifier_ligne).pack(pady=30)
 
# Delete functionality
frame_delete = tk.Frame(fenetre)
frame_delete.pack(pady=10)


fenetre.mainloop()
