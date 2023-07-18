def obtener_combinacion(mano):
    # Función que obtiene la combinación de manos de una mano de poker

    # Ordenamos las cartas por valor
    mano.sort()

    # Comprobamos si hay un flush
    if len(set([carta[1] for carta in mano])) == 1:
        flush = True
    else:
        flush = False

    # Comprobamos si hay una escalera
    escalera = False
    for i in range(len(mano) - 1):
        if mano[i][0] + 1 != mano[i + 1][0]:
            escalera = False
            break
        else:
            escalera = True

    # Comprobamos si hay un four of a kind
    four_of_a_kind = False
    for carta in mano:
        if mano.count(carta) == 4:
            four_of_a_kind = True
            break

    # Comprobamos si hay un full house
    full_house = False
    if set(mano.count(carta) for carta in mano) == {2, 3}:
        full_house = True

    # Comprobamos si hay un three of a kind
    three_of_a_kind = False
    for carta in mano:
        if mano.count(carta) == 3:
            three_of_a_kind = True
            break

    # Comprobamos si hay dos pares
    two_pair = False
    if list(mano.count(carta) for carta in mano).count(2) == 4:
        two_pair = True

    # Comprobamos si hay un par
    one_pair = False
    if 2 in list(mano.count(carta) for carta in mano):
        one_pair = True

    # Comprobamos si hay una carta alta
    high_card = True if not (flush or escalera or four_of_a_kind or full_house or three_of_a_kind or two_pair or one_pair) else False

    # Retornamos la combinación de manos correspondiente
    if flush and escalera:
        return "Straight flush"
    elif four_of_a_kind:
        return "Four of a kind"
    elif full_house:
        return "Full house"
    elif flush:
        return "Flush"
    elif escalera:
        return "Straight"
    elif three_of_a_kind:
        return "Three of a kind"
    elif two_pair:
        return "Two pair"
    elif one_pair:
        return "One pair"
    else:
        return "High card"


def comparar_manos(mano_jugador1, mano_jugador2, cartas_comunitarias):
    # Función que compara las combinaciones de manos de dos jugadores y determina el ganador

    # Combinamos las manos de los jugadores con las cartas comunitarias
    mano_total_jugador1 = mano_jugador1 + cartas_comunitarias
    mano_total_jugador2 = mano_jugador2 + cartas_comunitarias

    # Obtenemos las combinaciones de manos de cada jugador
    combinacion_jugador1 = obtener_combinacion(mano_total_jugador1)
    combinacion_jugador2 = obtener_combinacion(mano_total_jugador2)

    # Comparamos las combinaciones de manos y determinamos el ganador
    if combinacion_jugador1 == combinacion_jugador2:
        return "Empate"
    
mano_jugador1 = [(10, 'Picas'), (11, 'Corazones')]  # Mano del jugador 1: 10 de picas y J de corazones
mano_jugador2 = [(12, 'Diamantes'), (12, 'Treboles')]  # Mano del jugador 2: Q de diamantes y Q de tréboles
cartas_comunitarias = [(10, 'Treboles'), (11, 'Diamantes'), (12, 'Corazones'), (13, 'Picas'), (14, 'Diamantes')]  # Cartas comunitarias: 10 de tréboles, J de diamantes, Q de corazones, K de picas, A de diamantes

# Llamamos a la función comparar_manos para determinar el ganador
ganador = comparar_manos(mano_jugador1, mano_jugador2, cartas_comunitarias)

# Imprimimos el resultado
if ganador == "Empate":
    print("¡Es un empate!")
else:
    print(f"Gana el jugador {ganador}")   