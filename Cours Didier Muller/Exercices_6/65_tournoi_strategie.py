# dilemme du prisonnier itéré
# version tournoi

"""
Structure du code pour vos stratégies à envoyer en MP sous discord
Code à fournir par les apprenants:

# Stratégie qui consiste à coopérer tant que l'adversaire n'a pas trahi
def prénom(liste_lui, liste_moi):
    # Votre stratégie commentée
    return 'C'

liste['prénom'] = []
strategie['prénom'] = lambda lui, moi: prénom(lui, moi)
"""

from random import choice, seed



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
    return choice(['T', 'C'])


def donnant_donnant(liste_lui, liste_moi):
    """ Donnant donnant
        coopère seulement si l'autre joueur a coopéré au coup précédent.
    """
    if len(liste_lui) > 0:
        return liste_lui[-1]
    else:  # premier coup
        return 'C'

# Une partie entre deux joueurs différents

choix = ['T', 'C']  # T : trahit, C : coopère

liste = {}
strategie = {}
score = {}
duel = {}




liste['Bonne poire'] = []
liste['Aléatoire'] = []
liste['Donnant donnant'] = []

strategie['Bonne poire'] = lambda lui, moi: bonne_poire(lui, moi)
strategie['Aléatoire'] = lambda lui, moi: aleatoire(lui, moi)
strategie['Donnant donnant'] = lambda lui, moi: donnant_donnant(lui, moi)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ajouter des joueurs ci-dessous, selon les modèles des joueurs existants



# terminer là
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



nb_total_coups = 1000  # à modifier

for joueur in liste.keys():
    score[joueur] = 0

for i in liste.keys():  # i et j sont les joueurs
    for j in liste.keys():
        liste[i] = []   # on recommence une partie
        liste[j] = []
        if i >= j:
            nb_coups = 0
            score_joueur1 = 0
            score_joueur2 = 0
            seed(45226)  # germe du générateur aléatoire
            while nb_coups < nb_total_coups:
                coup_joueur1 = strategie[i](liste[j], liste[i])
                coup_joueur2 = strategie[j](liste[i], liste[j])
                liste[i].append(coup_joueur1)
                if i != j:
                    liste[j].append(coup_joueur2)
                score_joueur1 += gain(coup_joueur2, coup_joueur1)
                score_joueur2 += gain(coup_joueur1, coup_joueur2)
                nb_coups += 1
            duel[(i, j)] = score_joueur1
            if i != j:
                duel[(j, i)] = score_joueur2
            score[i] += score_joueur1
            if i != j:
                score[j] += score_joueur2

# affichage des résultats


def trie_par_valeur(d):
    # retourne une liste de tuples triée selon les valeurs
    return sorted(d.items(), key=lambda x: x[1])


def trie_par_cle(d):
    # retourne une liste de tuples triée selon les clés
    return sorted(d.items(), key=lambda x: x[0])


score_trie = trie_par_valeur(score)
score_trie.reverse()
for i in range(0, len(score_trie)):
    print('{:10d} : {}'.format(score_trie[i][1], score_trie[i][0]))
    # print(score_trie[i][0], ":", score_trie[i][1])
print()
duel_trie = trie_par_cle(duel)
for i in range(0, len(duel_trie)):
    print(duel_trie[i][0][0], "contre", duel_trie[i][0][1], "gagne", duel_trie[i][1], "pts")

print(duel)
for i in liste.keys():  # i et j sont les joueurs
    for j in liste.keys():
        if i!=j:
            print(i, j)
            print('duel[(i,j)]  duel[(j,i)', duel[(i,j)] , duel[(j,i)])
            if duel[(i,j)] > duel[(j,i)]:
                print('stratégie gagnante : ', i)
