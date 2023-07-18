import subprocess
import time
import tkinter as tk
from LetrasMano import contenido
from LetrasMano import contenidoPio
# from BuscarRangoSB import apuesta
from treys.card import Card
from treys.evaluator import Evaluator
from treys.deck import Deck
import mysql.connector


bet=0
bote=0
conexion = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="manos"
)
cursor = conexion.cursor()

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


# Ejecutar CardDetector.py
print("Ejecutando CardDetector.py...")
# card_detector_process = subprocess.Popen(["python", "CardDetector.py"])  # Ejecutar el proceso en segundo plano
from CardDetector import contenidoMano,contenidoMano2
time.sleep(3)
# card_detector_process.wait()  # Esperar a que se cierre el proceso

subprocess.run(["python", "searchhand.py"])
time.sleep(0.5)
from Orden import value1, value2,value3,value4
MiMano = (value1+value2+value3+value4)
print(MiMano)
# Ejecutar searchhand.py



# Ejecutar LetrasMano.py
print("Ejecutando LetrasMano.py...")
subprocess.run(["python", "LetrasMano.py"])
time.sleep(1)

if posicion=="SB":
    if len(MiMano) == 4:
    # Extrae la segunda y cuarta letra de la cadena
        segunda_letra = MiMano[1]
        cuarta_letra = MiMano[3]
        # Verifica si las dos letras coinciden en minúsculas
        if segunda_letra.lower() == cuarta_letra.lower():
            # Borra la segunda y cuarta letra y agrega una 's' al final de la cadena
            mano = MiMano[:1] + MiMano[2:3] + MiMano[4:] + "s"
        else:
            # Si las letras no coinciden, simplemente quita las letras
            mano = MiMano[:1] + MiMano[2:3]+ MiMano[4:] + "o"
        # Intentar leer el archivo LIMP_SB.txt
    print(mano)
    try:
        with open("LIMP_SB.txt", "r") as archivo:
            contenidoSB = archivo.read()

        # Buscar la cadena "mano" en el contenidoSB del archivo (ignorando mayúsculas y minúsculas)
        if mano.lower() in contenidoSB.lower().replace(",", " ").split():
            bet = 1
            consulta = "UPDATE tu_tabla SET bet = %s"  # Actualiza la columna 'bet' con el nuevo valor
            valores = (bet,)  # Convertir los valores a los tipos apropiados
            cursor.execute(consulta, valores)
            conexion.commit()
        else:
            raise FileNotFoundError  # Generar una excepción para que se intente el siguiente archivo

    # Si el archivo LIMP_SB.txt no existe, intentar con MR_SB.txt
    except FileNotFoundError:
        try:
            with open("MR_SB.txt", "r") as archivo:
                contenidoSB = archivo.read()

            # Establecer apuesta en 200 si encuentra la cadena "mano" en el archivo MR_SB.txt
            if mano.lower() in contenidoSB.lower().replace(",", " ").split():
                bet = 9
                consulta = "UPDATE tu_tabla SET bet = %s"  # Actualiza la columna 'bet' con el nuevo valor
                valores = (bet,)  # Convertir los valores a los tipos apropiados
                cursor.execute(consulta, valores)
                conexion.commit()
            else:
                bet = 500
                consulta = "UPDATE tu_tabla SET bet = %s"  # Actualiza la columna 'bet' con el nuevo valor
                valores = (bet,)  # Convertir los valores a los tipos apropiados
                cursor.execute(consulta, valores)
                conexion.commit()

        # Si tampoco existe el archivo MR_SB.txt, establecer apuesta en "fold"
        except FileNotFoundError:
            bet = 500



    #comando para pasar variable de bet y mover robot
    #sleep de unos segundos para dejar tiempo a que haga el movimiento
else :
    # Ejecutar BuscarRangosSB.py
    print("Ejecutando BuscarRangosBB.py...")
    BuscarRangosBB = subprocess.Popen(["python", "BuscarRangoBB.py"])  # Ejecutar el proceso en segundo plano

    BuscarRangosBB.wait()  # Esperar a que se cierre el proceso
    #comando para pasar variable de bet y mover robot
    #sleep de unos segundos para dejar tiempo a que haga el movimiento

# Ejecutar CardDetectorFlop.py
print("Ejecutando CardDetectorFlop.py...")
#card_detector_Flop_process = subprocess.Popen(["python", "CardDetectorFlop.py"])  # Ejecutar el proceso en segundo plano
from CardDetectorFlop import contenidoFlop,contenidoFlop2,contenidoFlop3
#card_detector_Flop_process.wait()  # Esperar a que se cierre el proceso
CartasFlop=(contenidoFlop+contenidoFlop2+contenidoFlop3)

print(CartasFlop)

# Ejecutar searchFlop.py
# print("Ejecutando searcFlop.py...")
# subprocess.run(["python", "searchFlop.py"])
# time.sleep(1)

# Ejecutar LetrasMano.py
# print("Ejecutando LetrasMano.py...")
# subprocess.run(["python", "LetrasMano.py"])
# time.sleep(1)


# Ejecutar los comandos en el terminal
print("Ejecutando comandos en el terminal...")
subprocess.run("python runme.py C:/PioSOLVER/PioSOLVER2-pro.exe C:/PioSOLVER/PioSolverConnection-master/python_2_0/HU8bbsQ85.cfr", shell=True)


time.sleep(1)
   
if posicion=="SB":
   
    
    # Ejecutar button.py
    # print("Ejecutando button.py...")
    # subprocess.run(["python", "button.py"])#Aqui se podria hacer un import del output del button.py para que sepa que hacer y dependiendo de la accion del rival hacer una cosa u otra
    from button import accion

    
    if accion=="Check":
         
        def Check_AI(MiMano):
            with open("calcevIPcb80.txt", "r") as archivo:
                contenido = archivo.read()
                indice = contenido.find(MiMano + ":")
                if indice != -1:
                    subcadena = contenido[indice + len(MiMano + ":"):]
                    numeroAI = subcadena.split(";")[0].strip()
                    return float(numeroAI)
                else:
                     return None
        
        numero_encontradoAI = Check_AI(MiMano)
                   
                
        def Check_Check(MiMano):
            with open("calcevIPcc.txt", "r") as archivo:
                contenido = archivo.read()
                indice = contenido.find(MiMano + ":")
                if indice != -1:
                    subcadena = contenido[indice + len(MiMano + ":"):]
                    numero = subcadena.split(";")[0].strip()
                    return float(numero)
                else:
                    return None  
        numero_encontradoCheck = Check_Check(MiMano)

        if numero_encontradoAI > numero_encontradoCheck:
            bet=8
            consulta = "UPDATE tu_tabla SET bet = %s"  # Actualiza la columna 'bet' con el nuevo valor
            valores = (bet,)  # Convertir los valores a los tipos apropiados
            cursor.execute(consulta, valores)
            conexion.commit()
            print("El robot decide hacer bet All In")
        else:
            print("El robot decide hacer Check")            
                
                
                
    elif accion=="b10":


        def Check_AI(MiMano):
            with open("calcevOOPB10AI.txt", "r") as archivo:
                contenido = archivo.read()
                indice = contenido.find(MiMano + ":")
                if indice != -1:
                    subcadena = contenido[indice + len(MiMano + ":"):]
                    numeroAI = subcadena.split(";")[0].strip()
                    return float(numeroAI)
                else:
                     return None
        
        numero_encontradoAI = Check_AI(MiMano)

        if numero_encontradoAI > 0:
            bet=8
            consulta = "UPDATE tu_tabla SET bet = %s"  # Actualiza la columna 'bet' con el nuevo valor
            valores = (bet,)  # Convertir los valores a los tipos apropiados
            cursor.execute(consulta, valores)
            conexion.commit()
            print("El robot decide hacer bet All In")
        else:
            bet=500
            consulta = "UPDATE tu_tabla SET bet = %s"  # Actualiza la columna 'bet' con el nuevo valor
            valores = (bet,)  # Convertir los valores a los tipos apropiados
            cursor.execute(consulta, valores)
            conexion.commit()
            print("El robot decide hacer Fold")

    elif accion=="b80":

        def Check_AI(MiMano):
            with open("calcevOOPB10AI.txt", "r") as archivo:
                contenido = archivo.read()
                indice = contenido.find(MiMano + ":")
                if indice != -1:
                    subcadena = contenido[indice + len(MiMano + ":"):]
                    numeroAI = subcadena.split(";")[0].strip()
                    return float(numeroAI)
                else:
                     return None
        
        numero_encontradoAI = Check_AI(MiMano)

        if numero_encontradoAI > 0:
            bet=8
            consulta = "UPDATE tu_tabla SET bet = %s"  # Actualiza la columna 'bet' con el nuevo valor
            valores = (bet,)  # Convertir los valores a los tipos apropiados
            cursor.execute(consulta, valores)
            conexion.commit()
            print("El robot decide hacer bet All In")
        else:
            bet=500
            consulta = "UPDATE tu_tabla SET bet = %s"  # Actualiza la columna 'bet' con el nuevo valor
            valores = (bet,)  # Convertir los valores a los tipos apropiados
            cursor.execute(consulta, valores)
            conexion.commit()
            print("El robot decide hacer Fold")
    #ejecutar solver para calcular vs accion del rival

    #luego ejecutar el robot para que haga la accion

    #posible boton por si tiene que seguir la accion el rival
    
    #Acaba el programa y se mostraria el resultado
    



if posicion=="BB":
    
    #ejecutar solver para calcular vs accion del rival
    
    #luego ejecutar el robot para que haga la accion

    # Ejecutar button.py
    print("Ejecutando button.py...")
    subprocess.run(["python", "button.py"])

    #Si el rival se tira: acaba el programa

    #si el rival paga: acaba tambien y se mostraria el resultado
    from CardDetectorTurn import contenidoTurn
    time.sleep(2)
    from CardDetectorRiver import contenidoRiver
    time.sleep(1)
    card = Card.new('Qh')

    # create a board and hole cards
    board = [
        Card.new(contenidoFlop),
        Card.new(contenidoFlop2),
        Card.new(contenidoFlop3),
        Card.new(contenidoTurn),
        Card.new(contenidoRiver)
    ]
    hand = [
        Card.new(contenidoMano),
        Card.new(contenidoMano2)
    ]
    hand2 = [
        Card.new('Js'),
        Card.new('2c')
    ]
    # pretty print cards to console
    Card.print_pretty_cards(board)
    Card.print_pretty_cards(hand)

    # create an evaluator
    evaluator = Evaluator()

    # and rank your hand
    rank = evaluator.evaluate(hand, board)
    class_ = evaluator.get_rank_class(rank)
    print("{} {}".format(rank, evaluator.class_to_string(class_)))
    print()

    # or for random cards or games, create a deck
    print("Dealing a new hand...")
    deck = Deck()
    board = board
    player1_hand = hand
    player2_hand = hand2

    print("The board:")
    Card.print_pretty_cards(board)

    print("Lorena's cards:")
    Card.print_pretty_cards(player1_hand)

    print("Player 2's cards:")
    Card.print_pretty_cards(player2_hand)

    p1_score = evaluator.evaluate(player1_hand, board)
    p2_score = evaluator.evaluate(player2_hand, board)

    # bin the scores into classes
    p1_class = evaluator.get_rank_class(p1_score)
    p2_class = evaluator.get_rank_class(p2_score)

    # or get a human-friendly string to describe the score
    print("Lorena hand rank = {} {}".format(p1_score, evaluator.class_to_string(p1_class)))
    print("Player 2 hand rank = {} {}".format(p2_score, evaluator.class_to_string(p2_class)))

    # or just a summary of the entire hand
    hands = [player1_hand, player2_hand]
    evaluator.hand_summary(board, hands)
