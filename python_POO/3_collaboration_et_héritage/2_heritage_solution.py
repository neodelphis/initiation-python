"""
Héritage simple et multiple dans le monde de l'âge de glace

Définir une classe Mammifere, qui contiendra deux caractéristiques nom et âge

A partir de cette classe, nous pourrons alors dériver une classe Primate, une classe Rongeur,
et une classe Carnivore, qui hériteront toutes les caractéristiques de la classe Mammifere.

Spécificités:
les rongeurs (comme scrat) pourront être initiés avec un nombre de glands
les carnivores pourront être initiés avec une caractéristique supplémentaire
('dents de sabre' pour Diego)


Définir une classe Herbivore dérivé de la classe Primate
Définir une classe Omnivore, qui hérite de la classe Carnivore et de la classe Herbivore

Instance de test à créer:
Mammifère: Manfred
Primate: Tarzan
Rongeur: Srat
Carnivore: Diego
Omnivore : Jane
"""


class Mammifere:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __repr__(self):
        return 'Mammifère ' + self.nom + ' de ' + str(self.age) + ' ans'


class Primate(Mammifere):
    def __repr__(self):
        return 'Primate ' + self.nom + ' de ' + str(self.age) + ' ans'
    pass


class Rongeur(Mammifere):
    def __init__(self, nom, age, nb_glands):
        Mammifere.__init__(self, nom, age)
        self.nb_glands = nb_glands

    def __repr__(self):
        return 'Rongeur : ' + self.nom + ' de ' + str(self.age) + ' ans' + ' avec ' + str(self.nb_glands) + ' gland(s)'


class Carnivore(Mammifere):
    def __init__(self, nom, age, caracteristique=None):
        Mammifere.__init__(self, nom, age)
        self.caracteristique = caracteristique
        print('Je suis un carnivore')

    def __repr__(self):
        return 'Carnivore : ' + self.nom + ' de ' + str(self.age) + ' ans' + ' avec ' + self.caracteristique


class Herbivore(Primate):

    def __init__(self):
        print('Je suis un Herbivore')


class Omnivore(Carnivore, Herbivore):
    def __init__(self, nom, age, caracteristique):
        Carnivore.__init__(self, nom, age, caracteristique)
        Herbivore.__init__(self)
        pass

    def __repr__(self):
        return 'Omnivore : ' + self.nom + ' de ' + str(self.age) + ' ans, ' + self.caracteristique


# Création d'un mammifère
mammouth = Mammifere('Manfred', 100)
print(mammouth)

# Création d'un primate
tarzan = Primate('Tarzan', 20)
print(tarzan)

# Création d'un rongeur avec surcharge de la méthode __init__
scrat = Rongeur('Srat', 5, 1)
print(scrat)

# Création d'un carnivore avec surcharge de la méthode __init__
diego = Carnivore('Diego', 20, 'dents de sabre')
print(diego)


print(Omnivore.__bases__)
jane = Omnivore('Jane', 20, 'compagne de Tarzan')
print(jane)
