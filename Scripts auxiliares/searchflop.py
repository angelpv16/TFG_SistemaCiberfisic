# Abre el archivo en modo lectura
with open("suit_rank_Flop.txt", "r") as archivo:
    contenidoFlopFlop = archivo.read()

# Crea un diccionario para mapear las palabras a sus iniciales en inglés
mapeo_iniciales = {
    "Hearts": "h",
    "Diamonds": "d",
    "Clubs": "c",
    "Spades": "s",
    "Ace": "A",
    "Two": "2",
    "Three": "3",
    "Four": "4",
    "Five": "5",
    "Six": "6",
    "Seven": "7",
    "Eight": "8",
    "Nine": "9",
    "Ten": "10",
    "Jack": "J",
    "Queen": "Q",
    "King": "K"
}

# Recorre el diccionario y reemplaza cada palabra encontrada por su inicial o número
for palabra, inicial in mapeo_iniciales.items():
    if inicial.isdigit():
        contenidoFlop = contenidoFlop.replace(palabra, inicial)
    else:
        contenidoFlop = contenidoFlop.replace(palabra, inicial[0])

# Busca las ocurrencias de ":" en el contenidoFlop y se queda solo con las letras o números después de los ":"
nuevo_contenidoFlop = ""
for linea in contenidoFlop.split("\n"):
    if ":" in linea:
        nuevo_contenidoFlop += linea.split(":")[1]
    else:
        nuevo_contenidoFlop += linea

# Separar cada dos letras o números por ";"
contenidoFlop_final = ""
for i in range(0, len(nuevo_contenidoFlop), 2):
    contenidoFlop_final += nuevo_contenidoFlop[i:i + 2] + ";"

# Abre el archivo en modo escritura para guardar los cambios
with open("suit_rank_flop.txt", "w") as archivo:
    archivo.write(contenidoFlop_final)

print("Se han reemplazado las palabras en el archivo con sus iniciales en inglés y números, se ha mantenido solo las letras o números después de los ':' en el archivo suit_rank_flop.txt, y se ha separado cada dos letras o números por ';' en el archivo.")
