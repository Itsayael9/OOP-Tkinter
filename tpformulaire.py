import tkinter as tk
from tkinter import messagebox

# Submit form to a pop-up window
def submit():
    name = name_entry.get()
    cni = cni_entry.get()
    gender = sex_var.get()
    region = liste.get(tk.ACTIVE)

    if not name or not cni or not gender or not region:
        messagebox.showerror("Error", "All fields must be filled!")
        return                 # Immediately stops the execution of the submit function if any of the required fields are empty

    # Create a pop-up related to the  window
    popup = tk.Toplevel(app)
    popup.title("Submitted Information")
    popup.geometry("300x200")
    popup.configure(bg="lightyellow")
    
    #le contenue des labels afficher dans le pop up 
           
    tk.Label(popup, text="Submission Details", bg="lightyellow").pack(pady=10)
    tk.Label(popup, text=f"Name: {name}", bg="lightyellow").pack(pady=5)
    tk.Label(popup, text=f"CNI: {cni}",bg="lightyellow").pack(pady=5)
    tk.Label(popup, text=f"Gender: {gender}", bg="lightyellow").pack(pady=5)
    tk.Label(popup, text=f"Region: {region}",  bg="lightyellow").pack(pady=5)

# Main window
app = tk.Tk()
app.title("Renovation de la carte nationale CNI")
app.geometry("500x400")
app.configure(bg="lightblue")

# label name 
name_label = tk.Label(app, text="Name:", font=("Arial", 16), fg="blue", bg="lightblue")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
# Input name
name_entry = tk.Entry(app, font=("Arial", 14))
name_entry.grid(row=0, column=1, padx=10, pady=10)
#cni label 
cni_label = tk.Label(app, text="CNI:", font=("Arial", 16), fg="blue", bg="lightblue")
cni_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
# cni input 
cni_entry = tk.Entry(app, font=("Arial", 14))
cni_entry.grid(row=1, column=1, padx=10, pady=10)

# pas de selection des radio 
sex_var = tk.StringVar(value="Aucun")
#label de gender  et grid 
sexe_label = tk.Label(app, text="Gender:", font=("Arial", 16), fg="blue", bg="lightblue")
sexe_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
# radio de femme et homme et grid 
radio1 = tk.Radiobutton(app, text="Male", variable=sex_var, value="Male", font=("Arial", 14), bg="lightblue")
radio2 = tk.Radiobutton(app, text="Female", variable=sex_var, value="Female", font=("Arial", 14), bg="lightblue")
radio1.grid(row=2, column=1, padx=10, pady=10, sticky="w")
radio2.grid(row=2, column=2, padx=10, pady=10, sticky="w")

# Region selection
liste_label = tk.Label(app, text="Select your region:", font=("Arial", 16), fg="blue", bg="lightblue")
liste_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
liste = tk.Listbox(app, font=("Arial", 14), height=4)
liste.insert(0, "Tanger-Tetouan-Al Hoceima")
liste.insert(1, "Rabat-Salé")
liste.insert(2, "Casablanca-Settat")
liste.grid(row=3, column=1, padx=10, pady=10)

# Submit button
submit_button = tk.Button(app, text="Submit", font=("Arial", 14), bg="green", fg="white", command=submit)
submit_button.grid(row=4, column=1, padx=10, pady=20)

# Run the app
app.mainloop()
