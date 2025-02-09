import tkinter as tk
from tkinter import messagebox

def pop_up():
    messagebox.showerror("Message", "Bonjour ! Tu as cliqué sur le bouton.")
#window principale 
window = tk.Tk()
window.title("Ma Première Fenêtre Tkinter")  
window.geometry("500x500") 

# label 
label = tk.Label(window, text="Bienvenue dans Tkinter !")
label.pack(pady=20)  #padding vertical 

# button
button = tk.Button(window, text="Clique-moi", command=pop_up)
button.pack(pady=10)


window.mainloop()