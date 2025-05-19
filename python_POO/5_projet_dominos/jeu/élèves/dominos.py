from random import randint


class Domino:

    # >>> Mettre votre code ici
    pass
    # <<<

    def peut_etre_place_a_gauche_de(self, valeur):
        if valeur == 0:
            return True
        if self.valeur_a_droite == valeur or self.valeur_a_droite == 0:
            return True
        else:
            return False

    def peut_etre_place_a_droite_de(self, valeur):
        if valeur == 0:
            return True
        if self.valeur_a_gauche == valeur or self.valeur_a_gauche == 0:
            return True
        else:
            return False


class Talon:

    # >>> Mettre votre code ici
    pass
    # <<<

    @classmethod
    def de_taille(cls, n):  # from_integer(cls, n):
        talon = cls([Domino() for _ in range(n)])
        return talon


class Chaine:

    # >>> Mettre votre code ici
    pass
    # <<<

class Main:

    # >>> Mettre votre code ici
    pass
    # <<<

    @classmethod
    def de_taille(cls, n):
        main = cls([Domino() for _ in range(n)])
        return main


class Joueur:
    def __init__(self, main=None):
        if main == None:
            self.main = Main()
        else:
            self.main = main
        self.chaine = None  # vue sur la chaîne

    def regarde_le_plateau(self, chaine):
        self.chaine = chaine

    def peut_jouer(self):
        if self.main.est_compatible(self.chaine.valeur_a_droite) or self.main.est_compatible(self.chaine.valeur_a_gauche):
            return True
        else:
            return False

    def choisit(self):
        raise NotImplementedError()

    def revendique_la_victoire(self):
        if len(self.main.m) == 0:
            return True
        else:
            return False


class Humain(Joueur):

    def __init__(self, main=None):
        self.type_de_joueur = 'HUMAIN'
        super().__init__(main)

    def affiche_main(self):
        # Affichage
        indices = ''
        for i in range(len(self.main.m)):
            indices += f'  {i+1}  '
        print(self.main, 'HUMAIN')
        print(indices)

    def choisit(self):
        position_impossible = True
        while position_impossible:
            # Affichage
            indices = ''
            for i in range(len(self.main.m)):
                indices += f'  {i+1}  '
            print(self.main, 'HUMAIN')
            print(indices)

            # Sélection
            position = 0
            while position not in range(1, len(self.main.m) + 1):
                position = int(input("Selectionner le "))
            domino = self.main.selectionne(position - 1)
            print(domino)

            # Inversion
            inversion = ''
            while inversion not in ['o', 'O', 'n', 'N']:
                inversion = input('Inverser [o/n]: ')
            if inversion in ['o', 'O']:
                domino.inverse()
                print(domino)

            # Placement avec test de validité du positionnement
            placement = ''
            while placement not in ['g', 'G', 'd', 'D']:
                placement = input('Placer à gauche (g) ou à droite (d) [g/d]: ')
            if placement in ['g', 'G']:
                placement = 'gauche'
                if domino.peut_etre_place_a_gauche_de(self.chaine.valeur_a_gauche):
                    position_impossible = False
                    self.main.retire(position - 1)
                else:
                    print('Positionnement impossible')
                    if inversion in ['o', 'O']:
                        domino.inverse()
            else:
                placement = 'droite'
                if domino.peut_etre_place_a_droite_de(self.chaine.valeur_a_droite):
                    position_impossible = False
                    self.main.retire(position - 1)
                else:
                    print('Positionnement impossible')
                    if inversion in ['o', 'O']:
                        domino.inverse()

        return domino, placement
