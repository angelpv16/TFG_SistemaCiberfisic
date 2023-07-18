############## Python-OpenCV Playing Card Detector ###############
#
# Author: Evan Juras
# Date: 9/5/17
# Description: Python script to detect and identify playing cards
# from a PiCamera video feed.
#

# Import necessary packages
import cv2
import numpy as np
import time
import os
import Cards
import VideoStream


### ---- INITIALIZATION ---- ###
# Define constants and initialize variables

## Camera settings
IM_WIDTH = 1280
IM_HEIGHT = 720 
FRAME_RATE = 10

## Initialize calculated frame rate because it's calculated AFTER the first time it's displayed
frame_rate_calc = 1
freq = cv2.getTickFrequency()

## Define font to use
font = cv2.FONT_HERSHEY_SIMPLEX

# Variable para controlar si la imagen está pausada o no
paused = False

# Initialize camera object and video feed from the camera. The video stream is set up
# as a seperate thread that constantly grabs frames from the camera feed. 
# See VideoStream.py for VideoStream class definition
## IF USING USB CAMERA INSTEAD OF PICAMERA,
## CHANGE THE THIRD ARGUMENT FROM 1 TO 2 IN THE FOLLOWING LINE:
videostream = VideoStream.VideoStream((IM_WIDTH,IM_HEIGHT),FRAME_RATE,2,0).start()
time.sleep(1) # Give the camera time to warm up

# Load the train rank and suit images
path = os.path.dirname(os.path.abspath(__file__))
train_ranks = Cards.load_ranks( path + '/Card_Imgs/')
train_suits = Cards.load_suits( path + '/Card_Imgs/')


### ---- MAIN LOOP ---- ###
# The main loop repeatedly grabs frames from the video stream
# and processes them to find and identify playing cards.

cam_quit = 0 # Loop control variable

# Begin capturing frames
while cam_quit == 0:
    if not paused:
        # Grab frame from video stream
        image = videostream.read()

    # Start timer (for calculating frame rate)
    t1 = cv2.getTickCount()

    # Pre-process camera image (gray, blur, and threshold it)
    pre_proc = Cards.preprocess_image(image)
	
    # Find and sort the contours of all cards in the image (query cards)
    cnts_sort, cnt_is_card = Cards.find_cards(pre_proc)

    # If there are no contours, do nothing
    if len(cnts_sort) != 0:

        # Initialize a new "cards" list to assign the card objects.
        # k indexes the newly made array of cards.
        cards = []
        k = 0

        # For each contour detected:
        for i in range(len(cnts_sort)):
            if (cnt_is_card[i] == 1):

                # Create a card object from the contour and append it to the list of cards.
                # preprocess_card function takes the card contour and contour and
                # determines the cards properties (corner points, etc). It generates a
                # flattened 200x300 image of the card, and isolates the card's
                # suit and rank from the image.
                cards.append(Cards.preprocess_card(cnts_sort[i],image))

                # Find the best rank and suit match for the card.
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


                # Print the suit and rank of the card
                # print("Suit of card", k+1, "is:", suit)
                # print("Rank of card", k+1, "is:", rank)
                with open('suit_rank_Flop.txt', 'w') as f:
                    for k in range(len(cards)):
                        f.write("{}:{}\n".format(k+1, cards[k].best_rank_match))
                        f.write("{}:{}\n".format(k+1, cards[k].best_suit_match))
                        

                
                # Draw center point and match result on the image.
                image = Cards.draw_results(image, cards[k])
                k = k + 1
	    
        # Draw card contours on image (have to do contours all at once or
        # they do not show up properly for some reason)
        if (len(cards) != 0):
            temp_cnts = []
            for i in range(len(cards)):
                temp_cnts.append(cards[i].contour)
            cv2.drawContours(image,temp_cnts, -1, (255,0,0), 2)
        
        
    # Draw framerate in the corner of the image. Framerate is calculated at the end of the main loop,
    # so the first time this runs, framerate will be shown as 0.
    cv2.putText(image,"FPS: "+str(int(frame_rate_calc)),(10,26),font,0.7,(255,0,255),2,cv2.LINE_AA)

    # Finally, display the image with the identified cards!
    cv2.imshow("Card Detector",image)

    # Calculate framerate
    t2 = cv2.getTickCount()
    time1 = (t2-t1)/freq
    frame_rate_calc = 1/time1
    
    # Poll the keyboard. If 'q' is pressed, exit the main loop.
    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        paused = not paused
    
    if key == ord("q"):
        cam_quit = 1
    
    # Si la variable k es igual a 3, se detiene la imagen pero no se cierra la ventana
    if k == 3 and cards[0].best_rank_match and cards[1].best_rank_match and cards[2].best_rank_match and cards[0].best_suit_match and cards[1].best_suit_match and cards[2].best_suit_match:
       
#CARTA 1    
        contenidoFlop = (cards[0].best_rank_match, cards[0].best_suit_match)

        contenidoFlop = list(contenidoFlop)  # Convertimos la tupla a lista para poder modificar los elementos

        for i in range(len(contenidoFlop)):
            for palabra, inicial in mapeo_iniciales.items():
                if contenidoFlop[i] == palabra:
                    contenidoFlop[i] = inicial
                elif isinstance(contenidoFlop[i], str):
                    contenidoFlop[i] = contenidoFlop[i].replace(palabra, inicial)

        contenidoFlop = "".join(contenidoFlop)  # Convertimos la lista nuevamente a cadena de texto

        print(contenidoFlop)

#CARTA 2
        contenidoFlop2 = (cards[1].best_rank_match, cards[1].best_suit_match)

        contenidoFlop2 = list(contenidoFlop2)  # Convertimos la tupla a lista para poder modificar los elementos

        for i in range(len(contenidoFlop2)):
            for palabra, inicial in mapeo_iniciales.items():
                if contenidoFlop2[i] == palabra:
                    contenidoFlop2[i] = inicial
                elif isinstance(contenidoFlop2[i], str):
                    contenidoFlop2[i] = contenidoFlop2[i].replace(palabra, inicial)

        contenidoFlop2 = "".join(contenidoFlop2)  # Convertimos la lista nuevamente a cadena de texto

        print(contenidoFlop2)

#CARTA 3       
        contenidoFlop3 = (cards[2].best_rank_match, cards[2].best_suit_match)

        contenidoFlop3 = list(contenidoFlop3)  # Convertimos la tupla a lista para poder modificar los elementos

        for i in range(len(contenidoFlop3)):
            for palabra, inicial in mapeo_iniciales.items():
                if contenidoFlop3[i] == palabra:
                    contenidoFlop3[i] = inicial
                elif isinstance(contenidoFlop3[i], str):
                    contenidoFlop3[i] = contenidoFlop3[i].replace(palabra, inicial)

        contenidoFlop3 = "".join(contenidoFlop3)  # Convertimos la lista nuevamente a cadena de texto

        print(contenidoFlop3)
    
        time.sleep(3)
        cam_quit = 1  

# Close all windows and close the PiCamera video stream.
cv2.destroyAllWindows()
videostream.stop()

