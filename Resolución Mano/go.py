from treys.card import Card
from treys.evaluator import Evaluator
from treys.deck import Deck
import subprocess
import time
import mysql.connector
from CardDetector import contenidoMano
from CardDetector import contenidoMano2
time.sleep(2)
from CardDetectorFlop import contenidoFlop,contenidoFlop2,contenidoFlop3
time.sleep(2)
from CardDetectorTurn import contenidoTurn
time.sleep(2)
from CardDetectorRiver import contenidoRiver



#importar las cartas obtenidas mediante camara


# create a card
card = Card.new('Qh')
bote1=150
bote2=150

ManoPropia=(contenidoMano+contenidoMano2)
ManoRival=('Js2c')
Board=(contenidoFlop+contenidoFlop2+contenidoFlop3+contenidoTurn+contenidoRiver)
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

conexion = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="manos"
)
cursor = conexion.cursor()
consulta = "INSERT INTO historialmanos (ManoPropia, ManoRival, Board, FichasPropias, FichasRival) VALUES (%s, %s, %s, %s, %s)"
valores = (str(ManoPropia), str(ManoRival), str(Board), int(bote1), int(bote2))  # Convert values to appropriate types
cursor.execute(consulta, valores)
conexion.commit()
cursor.close()
conexion.close()
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

