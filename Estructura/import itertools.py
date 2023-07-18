def reemplazar_texto(archivo_entrada, archivo_salida):
    # Diccionario de reemplazo
    sustituciones = {
        'KQ': 'KsQc,KsQh,KsQd,KcQs,KcQh,KcQd,KdQs,KdQc,KdQh,KhQs,KhQc,KhQd'
    }

    # Leer el archivo de entrada
    with open(archivo_entrada, 'r') as f:
        contenido = f.read()

    # Realizar las sustituciones
    for clave, valor in sustituciones.items():
        contenido = contenido.replace(clave, valor)

    # Escribir el archivo de salida
    with open(archivo_salida, 'w') as f:
        f.write(contenido)

# Archivos de entrada y salida
archivo_entrada = 'LIMP_SB.txt'
archivo_salida = 'LIMP_SB_sustituido.txt'

# Llamar a la función para realizar las sustituciones
reemplazar_texto(archivo_entrada, archivo_salida)
