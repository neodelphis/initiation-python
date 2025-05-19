"""
classe Ensemble
1. Créez une classe Ensemble pour représenter des sous-ensembles de l’ensemble des entiers compris entre 0 et N - 1,
   où N est une constante donnée strictement positive, avec les méthodes suivantes :
. contient(i) : test d’appartenance,
. ajoute(i) : ajout d’un élément à l’ensemble,
. __str__() : transformation de l’ensemble en une chaîne de caractères de la forme {5 , 6, 10, 15, 20, 21, 22, 30}

Les éléments d’un ensemble seront mémorisés dans une variable d’instance de type set().

Pour essayer la classe Ensemble, écrivez un programme déterminant les nombres différents et bornés par 0 et N
contenus dans une suite de nombres lue sur l’entrée standard.

2. Modifiez la classe précédente afin de permettre la représentation d’ensembles d’entiers quelconques,
c’est-à-dire non nécessairement compris entre 0 et une constante N connue à l’avance.
Faites en sorte que l’interface de cette classe soit identique à celle de la version précédente
 qu’il n’y ait rien à modifier dans les programmes qui utilisent la première version de cette classe.
"""


# class Ensemble:
#     def __init__(self, e, N):
#         """
#         Ensemble d'entiers compris entre 0 et N - 1
#         e : set()
#         N : integer
#         """
#         self.N = N
#         self.e = e.intersection(set(range(self.N)))

#     def contient(self, i):
#         return i in self.e

#     def ajoute(self, i):
#         if 0 <= i < self.N:
#             self.e.add(i)

#     def __str__(self):
#         representation = str(sorted(self.e))  # Par ordre croissant mais sous forme de liste avec []
#         representation = representation.replace('[', '{')
#         representation = representation.replace(']', '}')
#         return representation


# print("Cas d'un ensemble borné")
# mon_ensemble = Ensemble({-10, -3, 5, 6, 10, 15, 20, 21, 22, 30}, 20)
# print(mon_ensemble)
# mon_ensemble.ajoute(100)
# mon_ensemble.ajoute(-1)
# mon_ensemble.ajoute(1)
# print(mon_ensemble)

# mon_ensemble = Ensemble({5, 6, 10, 15, 20, 21, 22, 30}, 20)
# print(mon_ensemble)  # Appel à la méthode __str__
# print(mon_ensemble.contient(3))
# print(mon_ensemble.contient(5))
# print(mon_ensemble.ajoute(100))
# print(mon_ensemble.ajoute(-1))
# print(mon_ensemble.ajoute(1))
# print(mon_ensemble)

# N = int(input('N = '))
# entrees = []
# entree = 0
# while 0 <= entree < N:
#     entree = int(input('entrée = '))
#     if 0 <= entree < N:
#         entrees.append(entree)

# mon_ensemble = Ensemble(set(entrees), N)
# print(mon_ensemble)


# 2.
class Ensemble:
    def __init__(self, e, N=None):
        """
        Ensemble d'entiers compris entre 0 et N - 1 si N est renseigné
        Ensemble d'entiers quelconques sinon

        e : set()
        N : integer
        """
        self.N = N
        if self.N is None:
            self.e = e
        else:
            self.e = e.intersection(set(range(self.N)))

    def contient(self, i):
        return i in self.e

    def ajoute(self, i):
        if self.N is None:
            self.e.add(i)
        else:
            if 0 <= i < self.N:
                self.e.add(i)

    def __str__(self):
        representation = str(sorted(self.e))  # Par ordre croissant mais sous forme de liste avec []
        representation = representation.replace('[', '{')
        representation = representation.replace(']', '}')
        return representation


print("Cas d'un ensemble borné")
mon_ensemble = Ensemble({-10, -3, 5, 6, 10, 15, 20, 21, 22, 30}, 20)
print(mon_ensemble)
mon_ensemble.ajoute(100)
mon_ensemble.ajoute(-1)
mon_ensemble.ajoute(1)
print(mon_ensemble)

print("Cas d'un ensemble non borné")
mon_ensemble = Ensemble({-10, -3, 5, 6, 10, 15, 20, 21, 22, 30})
print(mon_ensemble)
mon_ensemble.ajoute(100)
mon_ensemble.ajoute(-1)
mon_ensemble.ajoute(1)
print(mon_ensemble)
