# Jeu de dominos à un seul joueur humain
from dominos import *
import os

# Fonction utilitaire
def efface_console():
    os.system('cls' if os.name=='nt' else 'clear')

# Initialisations
# # Cas jeu perdu
# humain = Humain([Domino(6, 5), Domino(1, 4)])
# chaine = Chaine()
# talon = Talon([])

# Cas jeu gagné par humain, pioche vide
# humain = Humain(Main([Domino(6, 6), Domino(6, 1)]))
# ordinateur = Ordinateur(Main([Domino(1, 1)]))
# chaine = Chaine()
# talon = Talon([])

# # Cas jeu gagné par ordinateur au décompte
# humain = Humain(Main([Domino(6, 6), Domino(3, 1)]))
# ordinateur = Ordinateur(Main([Domino(1, 1)]))
# chaine = Chaine()
# talon = Talon([])

# Cas aléatoire
humain = Humain(Main.de_taille(3))
ordinateur = Ordinateur(Main.de_taille(3))
chaine = Chaine()
talon = Talon.de_taille(4)


# Le jeu
efface_console()

# Qui commence?
if humain.main.plus_haute_valeur() >= ordinateur.main.plus_haute_valeur():  # tuple: 1er élément comparé
    joueurs = [humain, ordinateur]
else:
    joueurs = [ordinateur, humain]


joueur = joueurs[0]

premier_domino = joueur.main.domino_de_plus_haute_valeur()
print(f'{joueur.type_de_joueur} commence')
print('Premier domino', joueur.type_de_joueur, premier_domino)
chaine.pose_premier(premier_domino)
print(chaine, 'PLATEAU')
input("\nAppuyer sur une <Entréee> pour continuer")


# # Tours de jeu
fin = False
gagnant = False
numero_du_joueur = 1
liste_des_joueurs = [0, 1]


while not fin:
    joueur = joueurs[numero_du_joueur]
    efface_console()
    print(chaine, 'PLATEAU')
    joueur.regarde_le_plateau(chaine)
    if joueur.peut_jouer():
        domino, placement = joueur.choisit()
        chaine.ajoute(domino, placement)
        efface_console()
        print(chaine, 'PLATEAU')
        input()
        if joueur.revendique_la_victoire():
            fin = True
            print(f'Joueur {joueur.type_de_joueur} gagne')
            gagnant = True

    else:
        # Pioche dans le talon
        joueur.affiche_main()
        print(f'{joueur.type_de_joueur} n\'a pas de domino jouable. Pioche')
        domino = talon.pioche()
        if domino is None:
            print('Plus de dominos dans le talon')
            print('Passe')
            input()
            # On retire le joueur de la liste des joueurs autorisés à placer un domino
            liste_des_joueurs.remove(numero_du_joueur)
            if len(liste_des_joueurs) == 0:
                fin = True
        else:
            print(domino)
            joueur.main.ajoute(domino)
            if joueur.peut_jouer():
                print('Domino jouable')
                domino, placement = joueur.choisit()
                chaine.ajoute(domino, placement)
            else:
                print('Domino injouable')
                input()
    # Passage au joueur suivant
    if len(liste_des_joueurs) == 2 :
        numero_du_joueur = (numero_du_joueur + 1)%2
    elif len(liste_des_joueurs) == 1:
        numero_du_joueur = liste_des_joueurs[0]


# Initialisations différents cas
# Fin de partie en cas de talon vide
if len(liste_des_joueurs) == 0 and gagnant == False:
    print('Fin de partie en cas de talon vide')
    print(f'Humain {humain.main.score()}')
    print(f'Ordinateur {ordinateur.main.score()}')
    if humain.main.score() > ordinateur.main.score():
        print('ORDINATEUR gagne')
    elif humain.main.score() < ordinateur.main.score():
        print('HUMAIN gagne')
    else:
        print('Egalité')
