import tkinter as tk

def limpiar():
    global actRival, ventana
    actRival = "LIMP"
    ventana.destroy()

def mostrar():
    global actRival, ventana
    actRival = "MR"
    ventana.destroy()

def plegar():
    global actRival, ventana
    actRival = "fold"
    ventana.destroy()

def crear_ventana():
    global actRival, ventana
    actRival = ""

    ventana = tk.Tk()
    ventana.title("Botones")
    ventana.geometry("200x100")

    boton_limpiar = tk.Button(ventana, text="LIMP", command=limpiar)
    boton_limpiar.pack()

    boton_mostrar = tk.Button(ventana, text="MR", command=mostrar)
    boton_mostrar.pack()

    boton_plegar = tk.Button(ventana, text="fold", command=plegar)
    boton_plegar.pack()

    ventana.mainloop()

crear_ventana()
mano="Td4s"

if actRival == "LIMP":
    
    
    if len(mano) == 4:
        # Extrae la segunda y cuarta letra de la cadena
        segunda_letra = mano[1]
        cuarta_letra = mano[3]
        # Verifica si las dos letras coinciden en minúsculas
        if segunda_letra.lower() == cuarta_letra.lower():
            # Borra la segunda y cuarta letra y agrega una 's' al final de la cadena
            mano = mano[:1] + mano[2:3] + mano[4:] + "s"
        else:
            # Si las letras no coinciden, simplemente quita las letras
            mano = mano[:1] + mano[2:3]
    
    try:
        with open("CALL_LIMP_BB.txt", "r") as archivo:
            contenidoBB = archivo.read()

        # Buscar la cadena "mano" en el contenidoSB del archivo (ignorando mayúsculas y minúsculas)
        if mano.lower() in contenidoBB.lower().replace(",", " ").split():
            apuesta = "call"
        else:
            raise FileNotFoundError  # Generar una excepción para que se intente el siguiente archivo
    except FileNotFoundError:
        try:
            with open("ROL_BB.txt", "r") as archivo:
                contenidoBB = archivo.read()

            # Establecer apuesta en 200 si encuentra la cadena "mano" en el archivo MR_SB.txt
            if mano.lower() in contenidoBB.lower().replace(",", " ").split():
                apuesta = "AI"
            else:
                apuesta = "fold"

        # Si tampoco existe el archivo MR_SB.txt, establecer apuesta en "fold"
        except FileNotFoundError:
            apuesta = "fold"
elif actRival == "MR":
    
    mano="Td4s"
    if len(mano) == 4:
        # Extrae la segunda y cuarta letra de la cadena
        segunda_letra = mano[1]
        cuarta_letra = mano[3]
        # Verifica si las dos letras coinciden en minúsculas
        if segunda_letra.lower() == cuarta_letra.lower():
            # Borra la segunda y cuarta letra y agrega una 's' al final de la cadena
            mano = mano[:1] + mano[2:3] + mano[4:] + "s"
        else:
            # Si las letras no coinciden, simplemente quita las letras
            mano = mano[:1] + mano[2:3]
    
    try:
        with open("CALL_BB_VS_MR.txt", "r") as archivo:
            contenidoBB = archivo.read()

        # Buscar la cadena "mano" en el contenidoSB del archivo (ignorando mayúsculas y minúsculas)
        if mano.lower() in contenidoBB.lower().replace(",", " ").split():
            apuesta = "call"
        else:
            raise FileNotFoundError  # Generar una excepción para que se intente el siguiente archivo
    except FileNotFoundError:
        try:
            with open("BB_MR_ISO.txt", "r") as archivo:
                contenidoBB = archivo.read()

            # Establecer apuesta en 200 si encuentra la cadena "mano" en el archivo MR_SB.txt
            if mano.lower() in contenidoBB.lower().replace(",", " ").split():
                apuesta = "AI"
            else:
                apuesta = "fold"

        # Si tampoco existe el archivo MR_SB.txt, establecer apuesta en "fold"
        except FileNotFoundError:
            apuesta = "fold"
else:
    print("el rival ha foldeado")
    apuesta="ganas"
print("Valor de actRival:", actRival)
print("Valor de apuesta:", apuesta)
