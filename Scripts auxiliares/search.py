from LetrasMano import contenidoPio
# Nombre del archivo de texto
nombre_archivo = "output.txt"

# Cadena de caracteres a buscar
cadena_buscar = contenidoPio

# Variables para almacenar las acciones siguientes
action_oop = ""
action_ip = ""

# Contador de ocurrencias de la cadena buscada
contador = 0

# Abrir el archivo en modo lectura
with open(nombre_archivo, "r") as archivo:
    # Leer el contenido del archivo
    contenidoSearch = archivo.read()

    # Contar las ocurrencias de la cadena buscada
    contador = contenidoSearch.count(cadena_buscar)

    # Buscar la cadena de caracteres
    if contador > 0:
        # Obtener el índice del inicio de la primera cadena buscada
        inicio = contenidoSearch.index(cadena_buscar)

        # Obtener el índice del primer punto y coma después de la primera cadena buscada
        fin1 = contenidoSearch.index(";", inicio)

        # Extraer los caracteres siguientes hasta el primer punto y coma como acción OOP
        action_oop = contenidoSearch[inicio + len(cadena_buscar):fin1]

        # Obtener el índice del inicio de la segunda cadena buscada
        inicio2 = contenidoSearch.index(cadena_buscar, fin1)

        # Obtener el índice del primer punto y coma después de la segunda cadena buscada
        fin2 = contenidoSearch.index(";", inicio2)

        # Extraer los caracteres siguientes hasta el primer punto y coma como acción IP
        action_ip = contenidoSearch[inicio2 + len(cadena_buscar):fin2]

        print(f"La cadena '{cadena_buscar}' se encontró {contador} veces en el archivo.")
        print(f"La primera acción siguiente (OOP) es: {action_oop}")
        print(f"La segunda acción siguiente (IP) es: {action_ip}")
    else:
        print(f"La cadena '{cadena_buscar}' no se encontró en el archivo.")
