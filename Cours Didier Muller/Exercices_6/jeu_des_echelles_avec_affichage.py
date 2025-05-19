from random import randint

# Formalisation du jeu
# echelles dict du type { position_de_départ : position_d'arrivée}
# serpents idem.
echelles = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 51: 67, 71: 91, 80: 100}
serpents = {17: 7, 54: 34, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 79}


def sur_fin(position):
    return position == 100


def tour_de_jeu(position):
    # Lancer de dé
    lancer = randint(1, 6)
    nouvelle_position = position + lancer

    # Cas où on dépasse 100: on recule d'autant de cases que le dépassement
    if nouvelle_position > 100:
        nouvelle_position = 100 - (nouvelle_position - 100)

    # Gestion des échelles et des serpents
    if nouvelle_position in echelles:
        print(f'Nouvelle position temporaire : {nouvelle_position}, cool une échelle')
        print(f'Echelle : echelles[{nouvelle_position}] = {echelles[nouvelle_position]}')
        nouvelle_position = echelles[nouvelle_position]
    if nouvelle_position in serpents:
        print(f'Nouvelle position temporaire : {nouvelle_position}, oups un serpent')
        print(f'Serpent : serpents[{nouvelle_position}] = {serpents[nouvelle_position]}')
        nouvelle_position = serpents[nouvelle_position]
    return nouvelle_position


def une_partie():
    position = 0
    nombre_de_coups = 0
    while sur_fin(position) is False:
        print(position)
        position = tour_de_jeu(position)
        nombre_de_coups = nombre_de_coups + 1
    print('Gagné')

    return nombre_de_coups


print('Nombre de coups : ', une_partie())
