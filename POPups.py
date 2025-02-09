import tkinter as tk 
from tkinter import messagebox

def info():
    messagebox.showinfo("Informations","c'est une boite d'information")
#boite d'avertissment 
def warning():
    messagebox.showwarning("Avertissment","c'est une boite  d'avertisment ")
#boite d'erreur 
def error():
    messagebox.showerror("error","c'est une boite d'error ")
#boite de confirmation ok/cancel :
def confirmer1():
    reponse = messagebox.askokcancel("confirmation","souheter vous continuer ")
    if reponse:
        print("user a choix  de continuer ")
    else:
        print("user a annuler l'action ")
#boite de confirmation yes/no
def confirmer2():
    reponse = messagebox.askyesno("confirmation","etes vous sure ")
    if reponse :
        print("user a repondu YES ")
    else:
        print("user a repondu NO ")
        
#creatiion de la fenetre         
fenetre = tk.Tk()
#titre de la fenetre 
fenetre.title("boite de message ")

btn_info = tk.Button(fenetre,text="afficher info ",command=info, bg="lightblue",relief="ridge",fg="red")
btn_info.grid(row=0,column=0,pady=5,padx=5)

btn_warning = tk.Button(fenetre,text="afficher avertissment ",command=warning,bg="blue")
btn_warning.grid(row=0,column=1,pady=10,padx=10)

btn_error = tk.Button(fenetre,text="afficher error ",command=error)
btn_error.grid(row=1,column=0,pady=20,padx=20)

btn_ok_cancel = tk.Button(fenetre,text="ok/cancel",command=confirmer1,bg="yellow",font=("Arial", 12, "bold"))
btn_ok_cancel.grid(row=1,column=1,pady=5,padx=10)



btn_yes_no = tk.Button(fenetre,text="yes/no",command=confirmer2,relief="flat",fg="pink", cursor="hand2")
btn_yes_no.grid(row=2,column=0,pady=5,padx=10)

#background color of the window 

fenetre.configure(bg="pink")

fenetre.mainloop()

