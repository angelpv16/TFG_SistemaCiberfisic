# Leer el archivo suit_rank.txt
with open("suit_rank.txt", "r") as file:
    data = file.read().strip()

# Definir el diccionario de valores numéricos
numeric_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}

# Extraer los valores del string
value1 = data[0]
value2 = data[1]
value3 = data[2]
value4 = data[3]

# Asignar valores numéricos a las cartas
numeric_value1 = numeric_values.get(value1, int(value1) if value1.isdigit() else 0)
numeric_value3 = numeric_values.get(value3, int(value3) if value3.isdigit() else 0)

# Comparar los valores numéricos
if numeric_value3 > numeric_value1:
    # Intercambiar los valores
    value1, value3 = value3, value1

# Escribir los valores modificados en el archivo
with open("suit_rank.txt", "w") as file:
    file.write(value1 + value2 + value3 + value4)
