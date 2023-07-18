# Abre el archivo en modo lectura
with open("suit_rank.txt", "r") as archivo:
    contenido = archivo.read()
    contenidoPio=contenido
# Verifica si la longitud de la cadena es mayor o igual a 4 caracteres
if len(contenido) >= 4:
    # Extrae la segunda y cuarta letra de la cadena
    segunda_letra = contenido[1]
    cuarta_letra = contenido[3]
    # Verifica si las dos letras coinciden en minúsculas
    if segunda_letra.lower() == cuarta_letra.lower():
        # Borra la segunda y cuarta letra y agrega una 's' al final de la cadena
        contenido = contenido[:1] + contenido[2:3] + contenido[4:] + "s"

# Abre el archivo en modo escritura para guardar los cambios
with open("suit_rank.txt", "w") as archivo:
    archivo.write(contenido)

print("Se ha verificado y modificado el archivo suit_rank.txt según los requisitos indicados.")
