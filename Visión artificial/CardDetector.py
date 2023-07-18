import cv2
import numpy as np
import time
import os
import Cards
import VideoStream

# Definir constantes e inicializar variables

## Ajustes de la cámara
IM_WIDTH = 1280
IM_HEIGHT = 720 
FRAME_RATE = 10

## Inicializar la velocidad de fotogramas calculada porque se calcula DESPUÉS de la primera vez que se muestra
frame_rate_calc = 1
freq = cv2.getTickFrequency()

## Definir la fuente a usar
font = cv2.FONT_HERSHEY_SIMPLEX

# Variable para controlar si la imagen está pausada o no
paused = False

# Inicialice el objeto de la cámara y la transmisión de video desde la cámara. La transmisión de video está configurada.
# como un hilo separado que captura constantemente fotogramas de la transmisión de la cámara.
# Ver VideoStream.py para la definición de la clase VideoStream
## SI UTILIZA UNA CÁMARA USB EN LUGAR DE PICAMERA,
## CAMBIA EL TERCER ARGUMENTO DE 1 A 2 EN LA SIGUIENTE LINEA:
videostream = VideoStream.VideoStream((IM_WIDTH,IM_HEIGHT),FRAME_RATE,2,0).start()
time.sleep(1) # Give the camera time to warm up

# Cargue el rango del entrenamiento y las imágenes del palo.
path = os.path.dirname(os.path.abspath(__file__))
train_ranks = Cards.load_ranks( path + '/Card_Imgs/')
train_suits = Cards.load_suits( path + '/Card_Imgs/')


### ---- BUCLE PRINCIPAL ---- ###
# El bucle principal toma repetidamente frames de la transmisión de video
# y los procesa para encontrar e identificar naipes.

cam_quit = 0 # Loop control variable


while cam_quit == 0:
    if not paused:
       
        image = videostream.read()

    # Temporizador de inicio (para calcular la velocidad de fotogramas)
    t1 = cv2.getTickCount()
    k=0
    # Imagen de la cámara de preprocesamiento (gris, desenfoque y umbral)
    pre_proc = Cards.preprocess_image(image)
	
    # Encuentra y ordena los contornos de todas las tarjetas en la imagen (tarjetas de consulta)
    cnts_sort, cnt_is_card = Cards.find_cards(pre_proc)

    # Si no hay contornos, no hagas nada
    if len(cnts_sort) != 0:

        # Cree un objeto de carta a partir del contorno y agréguelo a la lista de cartas.
        
        cards = []
        k = 0

        # Para cada contorno detectado
        for i in range(len(cnts_sort)):
            if (cnt_is_card[i] == 1):

                # Cree un objeto de carta a partir del contorno y agréguelo a la lista de carta.
                 # la función preprocess_card toma el contorno de la carta y el contorno y
                 # determina las propiedades de las cartas (puntos de esquina, etc.). genera un
                 # imagen aplanada de 200x300 de la carta y aísla la carta
                 # palo y rango de la imagen.
                cards.append(Cards.preprocess_card(cnts_sort[i],image))

                # Encuentre la mejor combinación de rango y palo para la carta.
                cards[k].best_rank_match,cards[k].best_suit_match,cards[k].rank_diff,cards[k].suit_diff = Cards.match_card(cards[k],train_ranks,train_suits)
                

                suit = cards[k].best_suit_match
                rank = cards[k].best_rank_match
            

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
                    "Ten": "T",
                    "Jack": "J",
                    "Queen": "Q",
                    "King": "K"
                }
                
                with open('suit_rank.txt', 'w') as f:
                    for k in range(len(cards)):
                        f.write("{}:{}\n".format(k+1, cards[k].best_rank_match))
                        f.write("{}:{}\n".format(k+1, cards[k].best_suit_match))

                
                # Dibuje el punto central y haga coincidir el resultado en la imagen.
                image = Cards.draw_results(image, cards[k])
                k = k + 1
	    
        # Draw card contours on image (have to do contours all at once or
        # they do not show up properly for some reason)
        if (len(cards) != 0):
            temp_cnts = []
            for i in range(len(cards)):
                temp_cnts.append(cards[i].contour)
            cv2.drawContours(image,temp_cnts, -1, (255,0,0), 2)
        
        
    # Dibuja la velocidad de fotogramas en la esquina de la imagen. La velocidad de fotogramas se calcula al final del bucle principal,
     # así que la primera vez que esto se ejecuta, la velocidad de fotogramas se mostrará como 0.
    cv2.putText(image,"FPS: "+str(int(frame_rate_calc)),(10,26),font,0.7,(255,0,255),2,cv2.LINE_AA)

    # ¡Finalmente, muestra la imagen con las tarjetas identificadas!
    cv2.imshow("Card Detector",image)

    # Calcular la velocidad de fotogramas
    t2 = cv2.getTickCount()
    time1 = (t2-t1)/freq
    frame_rate_calc = 1/time1
    
   
    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        paused = not paused
    
    if key == ord("q"):
        cam_quit = 1

    


    # Si la variable k es igual a 2, se detiene la imagen pero no se cierra la ventana
    if k == 2 and cards[0].best_rank_match and cards[1].best_rank_match and cards[0].best_suit_match and cards[1].best_suit_match:
        
        contenidoMano = (cards[1].best_rank_match, cards[1].best_suit_match)

        contenidoMano = list(contenidoMano)  # Convertimos la tupla a lista para poder modificar los elementos

        for i in range(len(contenidoMano)):
            for palabra, inicial in mapeo_iniciales.items():
                if contenidoMano[i] == palabra:
                    contenidoMano[i] = inicial
                elif isinstance(contenidoMano[i], str):
                    contenidoMano[i] = contenidoMano[i].replace(palabra, inicial)

        contenidoMano = "".join(contenidoMano)  # Convertimos la lista nuevamente a cadena de texto

        print(contenidoMano)

        contenidoMano2 = (cards[0].best_rank_match, cards[0].best_suit_match)

        contenidoMano2 = list(contenidoMano2)  # Convertimos la tupla a lista para poder modificar los elementos

        for i in range(len(contenidoMano2)):
            for palabra, inicial in mapeo_iniciales.items():
                if contenidoMano2[i] == palabra:
                    contenidoMano2[i] = inicial
                elif isinstance(contenidoMano2[i], str):
                    contenidoMano2[i] = contenidoMano2[i].replace(palabra, inicial)

        contenidoMano2 = "".join(contenidoMano2)  # Convertimos la lista nuevamente a cadena de texto

        print(contenidoMano2)
        
        time.sleep(3)
        cam_quit = 1   


cv2.destroyAllWindows()
videostream.stop()

