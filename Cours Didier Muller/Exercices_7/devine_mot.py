# Exercice 7.2

from random import choice

# Récupération des mots
with open("liste_mots.txt", "r") as fichier:
    liste_mots = fichier.readlines()
    liste_mots = [mot.rstrip() for mot in liste_mots]

mot_a_deviner = choice(liste_mots)
# # Lettres triées par ordre alphabétique
# lettres_triees = ''
# for lettre in sorted(mot_a_deviner):
#     lettres_triees = lettres_triees + lettre
print(''.join(sorted(mot_a_deviner)))

mot_propose = ''
while mot_propose.upper() != mot_a_deviner:
    mot_propose = input("Quel est le mot correspondant? ")

print("Gagné")
