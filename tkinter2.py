import tkinter as tk 
app = tk.Tk()

def changer_message():
    global button 
    button.config(text="hello python ")
button = tk.Button(app,text="click here", command=changer_message)
button.pack(padx=100,pady=100)
app.mainloop()

