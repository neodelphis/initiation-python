from random import randint


class Domino:
    def __init__(self, valeur_a_gauche=None, valeur_a_droite=None):
        if valeur_a_gauche is None:
            valeur_a_gauche = randint(0, 6)
        if valeur_a_droite is None:
            valeur_a_droite = randint(0, 6)
        self.valeur_a_gauche = valeur_a_gauche
        self.valeur_a_droite = valeur_a_droite
        if (self.valeur_a_gauche not in range(7)) or \
                (self.valeur_a_droite not in range(7)):
            raise AttributeError('Valeur incorrecte pour le domino')

    def inverse(self):
        self.valeur_a_gauche, self.valeur_a_droite = self.valeur_a_droite, self.valeur_a_gauche
        return self

    def score(self):
        return self.valeur_a_gauche + self.valeur_a_droite

    def est_compatible(self, valeur):
        """
        Teste si le domino est compatible avec une valeur passée en paramètre
        c'est-à-dire s'il peut être placée à côté de cette valeur
        """
        if valeur == 0:
            return True
        if self.valeur_a_gauche == valeur or self.valeur_a_droite == valeur or self.valeur_a_gauche == 0 or self.valeur_a_droite == 0:
            return True
        else:
            return False

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

    def __repr__(self):
        if self.valeur_a_gauche == 0:
            valeur_a_gauche = ' '
        else:
            valeur_a_gauche = str(self.valeur_a_gauche)
        if self.valeur_a_droite == 0:
            valeur_a_droite = ' '
        else:
            valeur_a_droite = str(self.valeur_a_droite)

        return '['+valeur_a_gauche+':'+valeur_a_droite+']'

class Talon:
    """
    Talon (pioche) du jeu de domino
    """
    def __init__(self, t=None):
        if t is None:
            self.t = [Domino() for _ in range(10)]
        else:
            self.t = t

    def pioche(self):
        """
        Renvoie un domino qui est retiré du talon ou None s'il n'y en a plus de disponible
        """
        domino = None
        if self.t:
            domino = self.t.pop(0)
        return domino

    def __repr__(self):
        representation = ""
        if self.t:
            for domino in self.t:
                representation += repr(domino)
        return representation

    @classmethod
    def de_taille(cls, n):  # from_integer(cls, n):
        talon = cls([Domino() for _ in range(n)])
        return talon

class Chaine:
    """
    Représentation de la chaîne de jeu
    exemple: [1: ][3:5][5:2]
    Attributs:
    c : liste ordonnée des dominos selon le placement
    valeur_a_gauche : dans notre exemple 1
    valeur_a_droite : dans notre exemple 2
    """

    def __init__(self):
        self.c = []
        self.valeur_a_gauche = None
        self.valeur_a_droite = None

    def pose_premier(self, domino):
        self.c.insert(0, domino)
        self.valeur_a_gauche = domino.valeur_a_gauche
        self.valeur_a_droite = domino.valeur_a_droite

    def ajoute_au_cote_gauche(self, domino):
        self.c.insert(0, domino)
        self.valeur_a_gauche = domino.valeur_a_gauche

    def ajoute_au_cote_droit(self, domino):
        self.c.append(domino)
        self.valeur_a_droite = domino.valeur_a_droite

    def ajoute(self, domino, placement):
        if placement == 'gauche':
            self.ajoute_au_cote_gauche(domino)
        else:
            self.ajoute_au_cote_droit(domino)

    def __repr__(self):
        representation = ""
        if self.c:
            for domino in self.c:
                representation += repr(domino)
        return representation


class Main:
    """
    Gestion de la main du joueur
    m : liste de dominos
    """
    
    def __init__(self, m=None):
        if m is None:
            self.m = [Domino() for _ in range(5)]
        else:
            self.m = m

    def plus_haute_valeur(self):
        # Plus haute valeur dans la main du joueur
        score = None
        position = None
        if self.m:
            scores = [domino.score() for domino in self.m]
            score = max(scores)
            position = scores.index(score)
        return score, position

    def domino_de_plus_haute_valeur(self):
        # Extrait et renvoie le domino de plus haute valeur
        _, position_max = self.plus_haute_valeur()
        domino_choisi = None

        if position_max is not None:
            domino_choisi = self.m.pop(position_max)
        return domino_choisi
    
    def selectionne(self, indice):
        # Selectionne le domino tout en le laissant dans la main
        domino_choisi = self.m[indice]
        return domino_choisi

    def retire(self, indice):
        # Retire le domino de la main
        domino_choisi = self.m.pop(indice)
        return domino_choisi

    def est_compatible(self, valeur):
        # Renvoie vrai s'il y a un domino dans la main compatible avec la valeur passée en paramètre
        compatible = False
        if self.m:
            for domino in self.m:
                if domino.est_compatible(valeur):
                    compatible = True
                    break
        return compatible

    def ajoute(self, domino):
        self.m.append(domino)

    def score(self):
        s = 0
        if self.m:
            for domino in self.m:
                s += domino.score()
        return s

    def __repr__(self):
        representation = ""
        if self.m:
            for domino in self.m:
                representation += repr(domino)
        return representation

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
            while position not in range(1, len(self.main.m)+1):
                position = int(input("Selectionner le "))
            domino = self.main.selectionne(position-1)
            print(domino)

            # Inversion
            inversion = ''
            while inversion not in ['o','O', 'n', 'N']:
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
                    self.main.retire(position-1)
                else:
                    print('Positionnement impossible')
                    if inversion in ['o', 'O']:
                        domino.inverse()
            else:
                placement = 'droite'
                if domino.peut_etre_place_a_droite_de(self.chaine.valeur_a_droite):
                    position_impossible = False
                    self.main.retire(position-1)
                else:
                    print('Positionnement impossible')
                    if inversion in ['o', 'O']:
                        domino.inverse()

        return domino, placement


class Ordinateur(Joueur):

    def __init__(self, main=None):
        self.type_de_joueur = 'ORDINATEUR'
        super().__init__(main)

    def affiche_main(self):  # Seulement pour débug
        pass
        # # Affichage
        # indices = ''
        # for i in range(len(self.main.m)):
        #     indices += f'  {i+1}  '
        # print(self.main, 'ORDINATEUR')

    def choisit(self):
        # IA très basique
        # Teste les différentes possibilités de manière séquentielle
        for indice, domino in enumerate(self.main.m):
            if domino.peut_etre_place_a_gauche_de(self.chaine.valeur_a_gauche):
                domino_choisi = domino
                placement = 'gauche'
                break
            if domino.peut_etre_place_a_droite_de(self.chaine.valeur_a_droite):
                domino_choisi = domino
                placement = 'droite'
                break
            domino.inverse()
            if domino.peut_etre_place_a_gauche_de(self.chaine.valeur_a_gauche):
                domino_choisi = domino
                placement = 'gauche'
                break
            if domino.peut_etre_place_a_droite_de(self.chaine.valeur_a_droite):
                domino_choisi = domino
                placement = 'droite'
                break
        print(f'{self.type_de_joueur} joue {domino_choisi} à {placement}')
        input()
        del self.main.m[indice]
        return domino_choisi, placement


