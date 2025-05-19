# Micro-monde économique de la boulangerie
# Gestion d'une journée du micro monde

import time


class Produit:  # Classe abstraite
    def __init__(self):
        self.quantite = 0
        # 3 types de produits possibles
        #     Farine
        #     Blé
        #     Pain
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
        self.pain = Pain()

    def manger(self):
        if self.pain.quantite > 0:
            self.pain.quantite -= 1
            return True  # Mon personnage a reussi à manger
        else:
            return False  # Mon personnage n'a pas pu manger

    def produire(self):  # Méthode abstraite
        raise NotImplementedError()

    def recevoir(self, produit):  # Méthode commune
        if produit._type == 'Pain' and hasattr(self, 'pain'):
            self.pain.quantite += produit.quantite

        if produit._type == 'Blé' and hasattr(self, 'ble'):
            self.ble.quantite += produit.quantite

        if produit._type == 'Farine' and hasattr(self, 'farine'):
            self.farine.quantite += produit.quantite

    def livrer(self, produit, personnage):  # Méthode abstraite
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



    def livrer(self, produit, personnage):
        """
        Le paysan ne peut livrer que du blé, s'il en a suffisamment.
        Renvoie Vrai si la livraison a pu être effectuée
                Faux s'il n'y avait pas de stock
        """
        if produit._type == "Blé":
            if (self.ble.quantite - produit.quantite) >= 0:  # Quantité suffisante
                self.ble.quantite -= produit.quantite
                personnage.recevoir(produit)
                return True

        return False


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



    def livrer(self, produit, personnage):
        """
        Le meunier ne peut livrer que de la farine, s'il en a suffisamment.
        Renvoie Vrai si la livraison a pu être effectuée
                Faux s'il n'y avait pas de stock
        """
        if produit._type == "Farine":
            if (self.farine.quantite - produit.quantite) >= 0:  # Quantité suffisante
                self.farine.quantite -= produit.quantite
                personnage.recevoir(produit)
                return True

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



    def livrer(self, produit, personnage):
        """
        Le boulanger ne peut livrer que des pains, s'il en a suffisamment.
        Renvoie Vrai si la livraison a pu être effectuée
                Faux s'il n'y avait pas de stock
        """
        if produit._type == "Pain":
            if (self.pain.quantite - produit.quantite) >= 0:  # Quantité suffisante
                self.pain.quantite -= produit.quantite
                personnage.recevoir(produit)
                return True

        return False


class MicroMonde:

    def __init__(self):
        self.paysan = Paysan()
        self.meunier = Meunier()
        self.boulanger = Boulanger()

    def initialisation(self):
        # Tout le monde commence avec des pains
        self.paysan.pain.quantite = 1
        self.meunier.pain.quantite = 1
        self.boulanger.pain.quantite = 2
        # self.paysan.pain.quantite = 1
        # self.meunier.pain.quantite = 2
        # self.boulanger.pain.quantite = 5

    def journee(self):
        """
        Renvoie:
        Vrai si tous les personnages ont reussi à manger
        Faux si au moins un personnage n'a pas pu manger
        """
        WAIT = 1

        # Phase de production
        self.paysan.produire()
        self.paysan.produire()
        self.paysan.produire()

        # Le meunier produit tant qu'il a du blé
        while self.meunier.ble.quantite:
            self.meunier.produire()
        # Le boulanger produit tant qu'il a de la farine
        while self.boulanger.farine.quantite:
            self.boulanger.produire()
        time.sleep(WAIT)
        print('* Production')
        self.affiche()

        # Phase d'échange
        # Tout le monde livre le maximum de sa production
        # sauf le boulanger qui garde un pain pour le lendemain
        # le boulanger favorise toujours le paysan si c'est possible

        # Livraison du pain
        if self.boulanger.pain.quantite > 2:
            pain_a_livrer = Pain(self.boulanger.pain.quantite - 2)
            un_pain = Pain(1)
            while pain_a_livrer.quantite > 0:
                self.boulanger.livrer(un_pain, self.paysan)
                pain_a_livrer.quantite -= 1
                if pain_a_livrer.quantite > 0:
                    self.boulanger.livrer(un_pain, self.meunier)
                    pain_a_livrer.quantite -= 1

        # Livraison de la farine
        if self.meunier.farine.quantite > 0:
            farine_a_livrer = Farine(self.meunier.farine.quantite)
            self.meunier.livrer(farine_a_livrer, self.boulanger)

        # Livraison du blé
        if self.paysan.ble.quantite > 0:
            ble_a_livrer = Ble(self.paysan.ble.quantite)
            self.paysan.livrer(ble_a_livrer, self.meunier)
        time.sleep(WAIT)
        print('* Livraison')
        self.affiche()

        # Phase de repas
        tous_mangent = True  # On s'assure que tout le monde mange
        tous_mangent = tous_mangent * self.boulanger.manger()
        tous_mangent = tous_mangent * self.meunier.manger()
        tous_mangent = tous_mangent * self.paysan.manger()
        time.sleep(WAIT)
        print('* Repas')
        self.affiche()
        time.sleep(WAIT)

        return tous_mangent

    def simulation(self):
        self.initialisation()
        print('Etat initial')
        self.affiche()
        jour_suivant = True
        i = 1
        while jour_suivant:
            print('\nJour ', i)
            jour_suivant = self.journee()
            i += 1
        else:
            print('\nOups! Un personnage n\'a pas mangé à sa faim')

    def affiche(self):
        data = [['', 'Blé', 'Farine', 'Pain'],
                ['Paysan', str(self.paysan.ble.quantite), '',
                 str(self.paysan.pain.quantite)],
                ['Meunier', str(self.meunier.ble.quantite), str(
                    self.meunier.farine.quantite), str(self.meunier.pain.quantite)],
                ['Boulanger', '', str(self.boulanger.farine.quantite), str(self.boulanger.pain.quantite)]]
        col_width = max(len(word)
                        for row in data for word in row) + 2  # padding
        for row in data:
            print(''.join(word.ljust(col_width) for word in row))


# ### Programme Principal ### #

micro_monde = MicroMonde()
micro_monde.simulation()
