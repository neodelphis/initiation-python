# Micro-monde économique de la boulangerie
# Gestion de la production


class Produit:  # Classe abstraite
    def __init__(self):
        self.quantite = 0
        self._type = 'Produit non défini'  # Attribut protégé

    def __repr__(self):
        return self._type + ' : ' + str(self.quantite)


class Pain(Produit):
    def __init__(self, quantite=0):
        self.quantite = quantite
        self._type = 'Pain'  # Attribut protégé


class Ble(Produit):
    def __init__(self, quantite=0):
        Produit.__init__(self)
        self.quantite = quantite
        self._type = 'Blé'  # Attribut protégé


class Farine(Produit):
    def __init__(self, quantite=0):
        Produit.__init__(self)
        self.quantite = quantite
        self._type = 'Farine'  # Attribut protégé


class Personnage:  # Classe abstraite
    def __init__(self):
        # Tous les personnages peuvent posséder du pain
        # Chaque personnage commence le jeu avec 2 pains
        self.pain = Pain(2)

    def manger(self):
        if self.pain.quantite > 0:
            self.pain.quantite -= 1
            return True  # Mon personnage a reussi à manger
        else:
            return False  # Mon personnage n'a pas pu manger

    def produire(self):  # Méthode abstraite
        raise NotImplementedError()


class Paysan(Personnage):
    def __init__(self):
        Personnage.__init__(self)
        self.ble = Ble()

    def __repr__(self):
        representation = 'Paysan' + '\n\t' + \
            repr(self.pain) + '\n\t' +\
            repr(self.ble)
        return representation

    def produire(self):
        """
        Le Paysan produit du blé
        On considère que c'est toujours possible
        """
        self.ble.quantite += 1
        return True


class Meunier(Personnage):
    def __init__(self):
        Personnage.__init__(self)
        self.farine = Farine()
        self.ble = Ble()

    def __repr__(self):
        representation = 'Meunier' + '\n\t' + \
            repr(self.pain) + '\n\t' +\
            repr(self.ble) + '\n\t' +\
            repr(self.farine)
        return representation

    def produire(self):
        """
        Le meunier produit de la farine s'il a du blé
        renvoie: True s'il a pu produire
                 False sinon
        """
        if self.ble.quantite > 0:
            self.farine.quantite += 1
            self.ble.quantite -= 1
            return True
        else:
            return False


class Boulanger(Personnage):
    def __init__(self):
        Personnage.__init__(self)
        self.farine = Farine()

    def __repr__(self):
        representation = 'Boulanger' + '\n\t' + \
            repr(self.pain) + '\n\t' +\
            repr(self.farine)
        return representation

    def produire(self):
        """
        Le boulanger produit du pain s'il a de la farine
        renvoie: True s'il a pu produire
                 False sinon
        """
        if self.farine.quantite > 0:
            self.pain.quantite += 1
            self.farine.quantite -= 1
            return True
        else:
            return False


# ### Programme Principal ### #

# paysan = Paysan()
# print(paysan)
# paysan.produire()
# print(paysan)


# meunier = Meunier()
# print(meunier)
# meunier.ble.quantite = 1
# print(meunier)
# if meunier.produire():
#     print('Le meunier produit de la farine')
# else:
#     print('Production impossible, le meunier n\' a pas de blé')
# print(meunier)


boulanger = Boulanger()
boulanger.farine.quantite = 5

# while boulanger.produire():
#     print('Le boulanger produit du pain')
print(boulanger)
if boulanger.produire():
    print('Le boulanger produit du pain')
else:
    print('Production impossible, le boulanger n\' a pas de farine')
print(boulanger)

# print('Le boulanger mange si c\' est possible')
# boulanger.manger()
# print(boulanger)

if boulanger.produire():
    print('Le boulanger produit du pain')
else:
    print('Production impossible, le boulanger n\' a pas de farine')
print(boulanger)
