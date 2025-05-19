# Micro-monde économique de la boulangerie
# Sans utilisation des décorateurs pour définir les classes
# et méthodes abstraites


class Produit:  # Classe abstraite
    def __init__(self):
        self.quantite = 0
        self._type = 'Produit non défini'  # Attribut protégé

    def __repr__(self):
        return self._type + ' : ' + str(self.quantite)


class Pain(Produit):
    def __init__(self, quantite):
        self.quantite = quantite
        self._type = 'Pain'


class Personnage:  # Classe abstraite
    def __init__(self):
        # Chaque personnage commence le jeu avec 2 pains
        self.pain = Pain(2)

    def manger(self):
        """
        Renvoie:
        Vrai si le personnage a reussi à manger
        Faux si personnage n'a pas pu manger
        """
        if self.pain.quantite > 0:
            self.pain.quantite -= 1
            return True  # Mon personnage a reussi à manger
        else:
            return False  # Mon personnage n'a pas pu manger


class Paysan(Personnage):
    pass

    # ### Programme Principal ### #
# pain = Pain(2)
# print(pain)


paysan = Paysan()
while paysan.manger():
    print('J\'ai bien mangé')
    print('Pain restant : ', paysan.pain.quantite)
print('J\'ai faim')
