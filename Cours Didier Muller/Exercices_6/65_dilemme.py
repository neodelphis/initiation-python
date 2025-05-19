# dilemme du prisonnier itéré
# version duel
# T : trahit, C : coopère

from random import choice



def gain(lui, moi):
    if lui == 'C' and moi == 'C':
        return 3
    elif lui == 'C' and moi == 'T':
        return 5
    elif lui == 'T' and moi == 'C':
        return 0
    elif lui == 'T' and moi == 'T':
        return 1

# Fonctions décrivant les différentes stratégies

def toujours_seul(liste_lui, liste_moi):
    """ Toujours seul
        ne coopère jamais
    """
    return 'T'


def bonne_poire(liste_lui, liste_moi):
    """ Bonne poire
        coopère toujours
    """
    return 'C'


def aleatoire(liste_lui, liste_moi):
    """ Aléatoire
        joue avec une probabilité égale 'T' ou 'C'
    """
    global choix
    return choice(choix)


def donnant_donnant(liste_lui, liste_moi):
    """ Donnant donnant
        coopère seulement si l'autre joueur a coopéré au coup précédent.
    """
    if len(liste_lui) > 0:
        return liste_lui[-1]
    else:  # premier coup
        return 'C'


def majorite(liste_lui, liste_moi):
    """ Majorité
        coopère seulement si l'autre joueur a coopéré en majorité.
    """
    if len(liste_lui) > 0:
        if liste_lui.count('C') > len(liste_lui) // 2:
            return 'C'
        else:
            return 'T'
    else:  # premier coup
        return 'C'


def memoire_courte(liste_lui, liste_moi):
    """ Trahit si l'adversaire a trahi au moins une fois lors des 3 essais précédents
    """
    action = 'C'
    if len(liste_lui) > 3:
        if liste_lui[-3:].count('T') > 0:
            action = 'T'
    return action


nombre_trahison_consecutives = 0
nombre_trahison = 0


def teigneux(liste_lui, liste_moi):
    """ Coopère par défaut,
        mais trahit plusieurs fois à la suite et
        à chaque fois une fois supplémentaire dès que l'adversaire trahit
    """
    global nombre_trahison_consecutives
    global nombre_trahison

    action = 'C'
    if liste_lui:
        if liste_lui[-1] == 'T':
            nombre_trahison_consecutives += 1
            nombre_trahison += nombre_trahison_consecutives

    if nombre_trahison > 0:
        action = 'T'
        nombre_trahison -= 1

    return action


# Une partie entre deux joueurs différents
choix = ['T', 'C']  # T : trahit, C : coopère

liste = {}
score = {}

liste['joueur_1'] = []
liste['joueur_2'] = []

for joueur in liste.keys():
    score[joueur] = 0

nb_coups = 0
nb_total_coups = 100   # à modifier

while nb_coups < nb_total_coups:
    coup_joueur_1 = memoire_courte(liste['joueur_2'], liste['joueur_1'])
    # coup_joueur_1 = teigneux(liste['joueur_2'], liste['joueur_1'])
    # coup_joueur_2 = donnant_donnant(liste['joueur_1'], liste['joueur_2'])
    coup_joueur_2 = aleatoire(liste['joueur_1'], liste['joueur_2'])
    liste['joueur_1'].append(coup_joueur_1)
    liste['joueur_2'].append(coup_joueur_2)
    score['joueur_1'] += gain(coup_joueur_2, coup_joueur_1)
    score['joueur_2'] += gain(coup_joueur_1, coup_joueur_2)
    nb_coups += 1

for joueur in liste.keys():
    print("Coups et score du joueur", joueur)
    print(liste[joueur])
    print(score[joueur])
    print()
