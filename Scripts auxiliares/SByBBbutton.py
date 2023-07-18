import tkinter as tk

# Función para manejar el evento del botón "SB"
def guardar_sb():
    global posicion
    posicion = "SB"
    print("Posición:", posicion)
    ventana.destroy()  # Cerrar la ventana

# Función para manejar el evento del botón "BB"
def guardar_bb():
    global posicion
    posicion = "BB"
    print("Posición:", posicion)
    ventana.destroy()  # Cerrar la ventana

# Crear ventana
ventana = tk.Tk()
ventana.title("Botones")
ventana.geometry("250x100")  # Reducir el tamaño de la ventana a 250x100 píxeles

# Crear botón "SB"
boton_sb = tk.Button(ventana, text="SB", font=("Helvetica", 20), command=guardar_sb)
boton_sb.pack(side=tk.LEFT, padx=10)  # Colocar el botón a la izquierda con un espacio de 10 píxeles

# Crear botón "BB"
boton_bb = tk.Button(ventana, text="BB", font=("Helvetica", 20), command=guardar_bb)
boton_bb.pack(side=tk.LEFT, padx=10)  # Colocar el botón a la izquierda con un espacio de 10 píxeles

# Variable para guardar la posición
posicion = ""

# Iniciar bucle de eventos
ventana.mainloop()
