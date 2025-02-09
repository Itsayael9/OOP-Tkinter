import tkinter as tk

def afficher_selection():
  selction = var.get() #recupere la valeur  selectionnee
  label_resultat.config(text=f"Vous avez selectionne : {selction}") #affiche la valeur selectionnee

# Creation de la fenetre
app = tk.Tk()
app.title("Get Value from a Radio Button")

#variable pour stocker la variable selectionner
var = tk.StringVar(value="Aucune") # valeur par defaut


# Creation des boutons radio
radio1 = tk.Radiobutton(app, text="Option 1", variable=var, value="Option 1", command=afficher_selection)
radio2 = tk.Radiobutton(app, text="Option 2", variable=var, value="Option 2", command=afficher_selection)
radio3 = tk.Radiobutton(app, text="Option 3", variable=var, value="Option 3", command=afficher_selection)

radio1.pack()
radio2.pack()
radio3.pack()

#button pour afficher la selection 
button = tk.Button(app, text="Afficher la selection", command=afficher_selection)
button.pack(side=tk.RIGHT , padx=10 , pady=10) 

#label pour afficher le resultat
label_resultat = tk.Label(app, text="Resultat :")
label_resultat.pack()                

app.mainloop()