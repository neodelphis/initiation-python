"""
Polymorphisme
Ecrivez une classe Forme qui contiendra une méthode calcule_aire.
Faites-en hériter la classe Carre contenant un attribut `cote`
idem pour la classe Cercle contenant un attribut `rayon`
Rédéfinir la méthode calcul_aire pour les classes Carre et Cercle
Définir une fonction calcule_aire_totale qui à partir d’un tableau de `Forme`s calcule l’aire totale
"""
import math
# utilisation de math.pi pour le nombre Pi

class Forme:
    def calcule_aire():
        pass


class Carre(Forme):
    def __init__(self, cote):
        self.cote = cote

    def calcule_aire(self):
        return self.cote ** 2


class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calcule_aire(self):
        return math.pi * self.rayon ** 2

def calcule_aire_totale(formes):
    # Polymorphisme
    aire_totale = 0
    for forme in formes:
        aire_totale += forme.calcule_aire()
    return aire_totale


cercle_1 = Cercle(1)
print('cercle_1 : ', cercle_1.calcule_aire())

carre_2 = Carre(2)
print('carre_2 : ', carre_2.calcule_aire())


# Polymorphisme
formes = [cercle_1, carre_2]
aire_totale = calcule_aire_totale(formes)
assert calcule_aire_totale(formes) == 7.141592653589793
print('Aire totale pour l\'ensemble des formes', aire_totale)
