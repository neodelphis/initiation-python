import time
start_time = time.time()

# 7.5.g 
# Affichez tous les mots anacycliques : un mot lu de droite à gauche donne un autre mot.
# Par exemple : les – sel, bons – snob.

# Version optimisée.
# Il ne sert à rien de parcourir l'ensemble des mots à chaque fois
# Il faut juste parcourir la liste des mots de même ensemble de lettres

# Lecture du fichier
with open("dico.txt", "r") as fichier:
    dico = fichier.readlines()
    dico = [mot.rstrip() for mot in dico]
    
# Etape 1: On va créer un dictionnaire de type:
# {ensemble de lettres: liste des mots de cette longueur}
# l'objet defaultdict permet de faciliter la création de type de dictionnaire
from collections import defaultdict
mots_de_lettres = defaultdict(list)
for mot in dico:
    mots_de_lettres[tuple(sorted(list(set(mot))))].append(mot)

# Etape 2: On parcourt l'ensemble des mots

anacycliques = []
for mot in dico:
    if mot[::-1] in mots_de_lettres[tuple(sorted(list(set(mot))))] and mot[::-1] != mot:
        anacycliques.append(mot)

print('4g : ')
print(*anacycliques)

end_time = time.time()

print("Temps d'exécution : {} secondes.".format(end_time-start_time))
