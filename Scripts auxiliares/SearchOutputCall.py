def buscar_numero_archivo(mano):
    with open("calcevIPcb80.txt", "r") as archivo:
        contenido = archivo.read()
        indice = contenido.find(mano + ":")
        if indice != -1:
            subcadena = contenido[indice + len(mano + ":"):]
            numero = subcadena.split(";")[0].strip()
            return float(numero)
        else:
            return None

mano = "As9s"  # Puedes cambiar el valor de 'mano' aquí según tus necesidades
numero_encontrado = buscar_numero_archivo(mano)
print("Número encontrado:", numero_encontrado)

