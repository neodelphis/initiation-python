# Jeu à un joueur

Voici le dossier comprenant 2 fichiers pour finaliser le jeu à un joueur

Ce dossier comporte 2 fichiers

Vous devrez compléter le fichier `dominos.py` avec le code que vous avez développé lors du travail sur les notebooks (Attention aux copier-coller, car il faut garder certaines fonctions sur lesquelles je ne vous ai pas fait travailler).

A chaque fois je vous indique ou placer le code:

```
# >>> Mettre votre code ici
pass
# <<<
```

Pour lancer le jeu, se placer dans le dossier de travail et faire
`python un_joueur.py`

Si vous regardez dans le fichier `un_joueur.py` vous avez un lot d'initialisations pour tester les différents cas:

```
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
```

Testez les 3 cas pour voir si tout marche comme il faut.
