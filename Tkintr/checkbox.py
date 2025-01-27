import tkinter as tk

app = tk.Tk()
app.title("Checkbox Example")
app.geometry("300x200")

checkbox = tk.Checkbutton(app, text="I agree to the terms and conditions")
checkbox.pack(pady=20)

app.mainloop()
