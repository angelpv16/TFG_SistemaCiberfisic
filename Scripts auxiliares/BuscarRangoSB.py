# Definir la mano a buscar

mano='AhAd'
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
        mano = mano[:1] + mano[2:3]+mano[4:]+ "o"
# Intentar leer el archivo LIMP_SB.txt
print(mano)
try:
    with open("LIMP_SB.txt", "r") as archivo:
        contenidoSB = archivo.read()

    # Buscar la cadena "mano" en el contenidoSB del archivo (ignorando mayúsculas y minúsculas)
    if mano.lower() in contenidoSB.lower().replace(",", " ").split():
        apuesta = "call"
    else:
        raise FileNotFoundError  # Generar una excepción para que se intente el siguiente archivo

# Si el archivo LIMP_SB.txt no existe, intentar con MR_SB.txt
except FileNotFoundError:
    try:
        with open("MR_SB.txt", "r") as archivo:
            contenidoSB = archivo.read()

        # Establecer apuesta en 200 si encuentra la cadena "mano" en el archivo MR_SB.txt
        if mano.lower() in contenidoSB.lower().replace(",", " ").split():
            apuesta = "8"
        else:
            apuesta = "fold"

    # Si tampoco existe el archivo MR_SB.txt, establecer apuesta en "fold"
    except FileNotFoundError:
        apuesta = "fold"

# Imprimir el valor de la variable apuesta
print("Apuesta:", apuesta)
