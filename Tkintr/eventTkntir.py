import tkinter as tk

def key_event(event):
    label.config(text=f"Touche presse : {event.char}")

def button_click(event):
    label.config(text=f"Clic souris detecte : Bouton {event.num} à ({event.x}, {event.y})")

def button_release(event):
    label.config(text=f"Bouton {event.num} relâché")

def double_click(event):
    label.config(text=f"Double clic détecté : Bouton {event.num}")

def mouse_motion(event):
    label.config(text=f"Déplacement de la souris à ({event.x}, {event.y})")

def mouse_enter(event):
    label.config(text="La souris est entrée dans la zone !")

def mouse_leave(event):
    label.config(text="La souris a quitté la zone !")


root = tk.Tk()
root.title("Événements de la souris et du clavier")

label = tk.Label(root, text="Interagissez avec la fenêtre")
label.pack()


root.bind("<Key>", key_event)    #tout touche de clavier          
root.bind("<Button-1>", button_click) # click gauche     
root.bind("<Button-2>", button_click) # click melieu 
root.bind("<Button-3>", button_click) # click droit 
root.bind("<ButtonRelease-1>", button_release)  # relachement clic gauche 
root.bind("<Double-Button-1>", double_click)  # double clic gauche 
root.bind("<Motion>", mouse_motion)  # deplacement de la souris   
label.bind("<Enter>", mouse_enter)  # entre souris     
label.bind("<Leave>", mouse_leave) # sourtie de la souris     


root.mainloop()