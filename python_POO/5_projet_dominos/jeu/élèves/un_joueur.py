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

# # Cas jeu gagné
# humain = Humain([Domino(6, 5), Domino(1, 4)])
# chaine = Chaine()
# talon = Talon([Domino(5,3), Domino(1, 3)])

# Cas aléatoire
main = Main.de_taille(3)
humain = Humain(main)
chaine = Chaine()
talon = Talon.de_taille(2)


# Le jeu
efface_console()
joueur = humain
joueur.affiche_main()

premier_domino = joueur.main.domino_de_plus_haute_valeur()
print('Premier domino', 'HUMAIN', premier_domino)
chaine.pose_premier(premier_domino)
print(chaine, 'PLATEAU')
input("\nAppuyer sur une <Entréee> pour continuer")


# Tours de jeu
fin = False

while not fin:
    efface_console()
    print(chaine, 'PLATEAU')
    joueur.regarde_le_plateau(chaine)
    if joueur.peut_jouer():
        domino, placement = joueur.choisit()
        chaine.ajoute(domino, placement)
        efface_console()
        print(chaine, 'PLATEAU')
        if joueur.revendique_la_victoire():
            fin = True
            print('Joueur HUMAIN gagne')

    else:
        # Pioche dans le talon
        joueur.affiche_main()
        print('Pas de domino jouable. Pioche')
        domino = talon.pioche()
        if domino is None:
            print('Plus de dominos dans le talon')
            print('Perdu')
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


# Pseudo-code
#
# joueur.main.domino_de_plus_haute_valeur()
# chaine.pose_premier(premier_domino)
#
# Tant que la partie n'est pas finie
#     joueur.regarde_le_plateau(chaine)
#     joueur.peut_jouer()?
#     - oui
#         domino, placement = joueur.choisit()
#         chaine.ajoute(domino, placement)
#         joueur.revendique_la_victoire() ?
#     - non
#         Pioche dans le talon
#         domino = talon.pioche()
#         Plus de dominos dans le talon? Fin
#         joueur.main.ajoute(domino)
#         joueur.peut_jouer()?
#         - oui
#         domino, placement = joueur.choisit()
#         chaine.ajoute(domino, placement)
#         - non
