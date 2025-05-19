# dilemme du prisonnier itéré
# version tournoi

"""
Pour le tournoi `Exercice 6.5 – Tournoi`, voici la structure du code pour vos stratégies à envoyer en MP sous discord

```py
def prenom(liste_lui, liste_moi):
    # Explications de ma super stratégie:
    # Je coopère toujours
    return 'C'

liste['prenom'] = []
strategie['prenom'] = lambda lui, moi: prenom(lui, moi)
```
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


def radical(liste_lui, liste_moi):
    """ Trahit tout le temps dès que l'adversaire a trahi au moins une fois
    """
    action = 'C'
    if liste_lui.count('T') > 0:
        action = 'T'
    return action


def tit_for_tat(liste_lui, liste_moi):
    """Cooperates on the first round and imitates its opponent's previous move thereafter.
    """
    if len(liste_lui) == 0:
        return 'C'
    else:
        return liste_lui[-1]


# Une partie entre deux joueurs différents

choix = ['T', 'C']  # T : trahit, C : coopère

liste = {}
strategie = {}
score = {}
duel = {}




liste['Toujours seul'] = []
liste['Bonne poire'] = []
liste['Majorité'] = []
liste['Aléatoire'] = []
liste['Donnant donnant'] = []
liste['memoire_courte'] = []
liste['teigneux'] = []
liste['radical'] = []
liste['tit_for_tat'] = []

strategie['Toujours seul'] = lambda lui, moi: toujours_seul(lui, moi)
strategie['Bonne poire'] = lambda lui, moi: bonne_poire(lui, moi)
strategie['Majorité'] = lambda lui, moi: majorite(lui, moi)
strategie['Aléatoire'] = lambda lui, moi: aleatoire(lui, moi)
strategie['Donnant donnant'] = lambda lui, moi: donnant_donnant(lui, moi)
strategie['memoire_courte'] = lambda lui, moi: memoire_courte(lui, moi)
strategie['teigneux'] = lambda lui, moi: teigneux(lui, moi)
strategie['radical'] = lambda lui, moi: teigneux(lui, moi)
strategie['tit_for_tat'] = lambda lui, moi: tit_for_tat(lui, moi)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ajouter des joueurs ci-dessous, selon les modèles des joueurs existants

#Maëlle
#coopere premier coup
#donnant-donnant pour le deuxieme coup
#puis majorite pour le troisieme coup (qui reprend les trois derniers coups)
def maelle(liste_moi, liste_lui):

    # premier coup
    if len(liste_moi) == 0:
        return 'C'

    # deuxieme coup
    elif len(liste_lui) == 1 :
        print(liste_lui[-1])
        return liste_lui[-1]

    # >>>>>
    # Il te manque le cas len(liste_lui) == 2
    # du coup ça palnte car tu ne retournes rien dans ce cas

    if len(liste_moi) == 2:
        return 'C'
    # <<<<<


    # troiseme coup  # C'est le 4ème
    elif len(liste_lui) > 2:
        liste3_derniers = []
        liste3_derniers.append(liste_lui[-1])
        liste3_derniers.append(liste_lui[-2])
        liste3_derniers.append(liste_lui[-3])
        if liste3_derniers.count('C') >= len(liste3_derniers)//2:
            return 'C'
        else:
            return 'T'


liste['maelle'] = []
strategie['maelle'] = lambda lui, moi: maelle(lui, moi)  # Il faut que tu appelles ta fonction pas "prenom"


# def rudy(liste_lui,liste_moi):
#     # Snitch
#     # spill the bill

#     return 'T'

# liste['rudy'] = []
# strategie['rudy'] = lambda lui, moi : rudy(lui,moi)


# def rayan(liste_lui,liste_moi):
#     #Coopere jusqu'a ce qu'il se fasse trahir et trahit jusqu'a la fin
#     if len(liste_lui) > 0:
#         for i in liste_lui:
#             if i == 'T':
#                 return 'T'
#     return 'C'

# liste['rayan'] = []
# strategie['rayan'] = lambda lui, moi: rayan(lui, moi)


# def eric(liste_lui,liste_moi):
# # je coopère tant que l'autre prisonnier ne m'a pas trahi
#     if len(liste_lui)>0:
#         if liste_lui.count('C') == 0: # dès que le prisonnier me trahit une fois, je le trahi pour le reste de la partie
#             return 'C'
#         else:
#             return 'T'
#     else: # premier coup
#         return 'C'

# liste['Eric'] = []
# strategie['Eric'] = lambda lui, moi : eric(lui,moi)


# def Allan(liste_lui, liste_moi):
# #Rancune:
# #A la moindre trahison, trahit jusqu'à la fin
#     if 'T'in liste_lui:
#         return 'T'
#     else:
#         return 'C' 

# liste['Allan']=[]
# strategie['Allan']=lambda lui,moi : Allan(lui,moi)


# #Pascale -> coopère seulement si l'autre joueur a coopéré plus de 2 fois qu'il n'a trahi
# def pascale(liste_lui, liste_moi):
#     if liste_lui.count('C') >= 2*liste_lui.count('T'):
#         return 'C'
#     else:
#         return 'T'

# liste['Pascale'] = []
# strategie['Pascale'] = lambda lui, moi: pascale(lui, moi)


# def yvan(liste_lui, liste_moi):
#         if len(liste_moi)==0:#premier coup, on coopère
#             strategie
#             return'C'

#         elif len(liste_moi)==1:                 #deuxième coup, on trahit
#             return 'T'

#         elif len(liste_moi)==2:                 #toisième coup, on entrevoit une stratégie
#             if liste_lui.count('T')!=0:         #s'il a trahit a n2, il est soit méchant, soit aléatoire
#                 strategie['yvan']=lambda lui, moi : toujours_seul(lui,moi)    #on a tout intérêt à devenir méchant
#                 return 'T'
#             else :
#                 return 'C'                      #sinon on coopère

#         elif len(liste_moi)==3:                 #quatrième coup, on détermine la stratégie
#             if liste_lui[2]=='T':               #s'il a trahit au troisième coup, il est soit DD, soit Maj, peut être aléatoire....
#                 strategie['yvan']=lambda lui, moi : bonne_poire(lui,moi) #on coopère
#                 return 'C'
#             else:                               #s'il a coopéré alors que j'avait trahit, c'est un pigeon
#                 strategie['yvan']=lambda lui, moi : toujours_seul(lui,moi)    #on le plume
#                 return 'T'
#     #on devrait trahir toujours la dernière fois

# liste['yvan'] = []
# strategie['yvan'] = lambda lui, moi: yvan(lui, moi)

# def Cesar(liste_lui, liste_moi):
# #Toujours coopérer avec les personnes nayant pas trahis
# #Trahir les personnes ayant trahit au moins une fois
# #Toujours trahir le dernier tour
#     len(liste_lui)+1== nb_total_coups
#     if len(liste_lui)>0:
#         if liste_lui.count('T'): 
#             return 'T'
#         else:
#             if len(liste_lui)+1== nb_total_coups:
#                 return 'T'
#             else:
#                 return 'C'
            
#     else: 
#         return 'C'
# liste['Cesar'] = []
# strategie['Cesar'] = lambda lui, moi : Cesar(lui,moi)

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

# print(duel)
