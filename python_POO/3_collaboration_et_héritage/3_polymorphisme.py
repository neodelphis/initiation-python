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



cercle_1 = Cercle(1)
print('cercle_1 : ', cercle_1.calcule_aire())

carre_2 = Carre(2)
print('carre_2 : ', carre_2.calcule_aire())


# Polymorphisme
formes = [cercle_1, carre_2]
aire_totale = calcule_aire_totale(formes)
assert calcule_aire_totale(formes) == 7.141592653589793
print('Aire totale pour l\'ensemble des formes', aire_totale)
