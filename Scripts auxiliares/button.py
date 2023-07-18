import tkinter as tk
from tkinter import ttk
import subprocess

accion = ""  # Declarar accion como una variable global

def bet10_button_callback():
    # Codigo que se ejecuta cuando se pulse el boton "Bet10"
    global accion  # Declaro la variable accion como global
    print("bet10")
    accion = "bet10"
    root.destroy()

def Check_button_callback():
    # Code que se ejecuta cuando se pulsa el boton de check
    global accion  # Declaro la variable accion como global
    print("Check")
    accion = "Check"
    root.destroy()

def bet80_button_callback():
    # Codigo que se ejecuta cuando se pulsa el boton de bet80
    global accion  # Declaro la variable accion como global
    print("bet80")
    accion = "bet80"
    root.destroy()

root = tk.Tk()

# Crea un frame para colocar los botones
subframe = tk.Frame(root)
subframe.pack()
# Crea el boton de check
fold_button = ttk.Button(subframe, text="Check", command=Check_button_callback, style="TButton")
fold_button.pack(side=tk.LEFT, padx=5)

# Create el boton de bet10
call_button = ttk.Button(subframe, text="bet10", command=bet10_button_callback, style="TButton")
call_button.pack(side=tk.LEFT, padx=5)

# Crea el boton de bet80
bet_button = ttk.Button(subframe, text="Bet80", command=bet80_button_callback, style="TButton")
bet_button.pack(side=tk.LEFT)

root.mainloop()



