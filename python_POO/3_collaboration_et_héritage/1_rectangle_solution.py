"""
1. Définir la classe Point contenant les attributs x et y (coordonnées)
   Implémenter une méthode permettant un affichage sous forme de string du type "(x, y)"
   Implémenter la  méthode __del__ qui affichera "Point détruit"

2. Définir la classe Rectangle
   Pour définir un rectangle, nous spécifions sa largeur, sa hauteur et précisons la position du coin supérieur gauche.
   Une position est définie par un point (coordonnées x et y).
   On s'assurera dans le constructeur que largeur et hauteur sont supposés être des réels positifs.
   Dans le cas contraire ils prendront la valeur 0 par défaut.
   Ils doivent être supérieurs ou égaux à zéro, sinon on mets la valeur 0 par défaut.
   Les modifications sont possibles, on s'assurera simplement que le réel passé est positif,
   dans le cas contraire on ne fera pas de modification.
   Implémenter une méthode permettant un affichage sous forme de string du type "L: 50, H: 36, Coin: (12, 25)"
   Implémenter la  méthode __del__ qui affichera "Rectangle détruit"

3. Instancier un objet mon_rectangle de largeur 4, de hauteur 6, et dont le coin supérieur
   gauche se situe au point de coordonnées (2, 10)
   Tester les différentes méthodes codées

4. Nous avons vu plus haut que les fonctions peuvent utiliser des objets comme paramètres.
   Elles peuvent également transmettre une instance comme valeur de retour.
   Définir la fonction trouveCentre() qui est appelée avec un argument de type Rectangle
   et qui renvoie un objet Point, lequel contiendra les coordonnées du centre du rectangle.

   Tester cette fonction en utilisant l’objet mon_rectangle défini
"""
class Point:
    """ Point défini par ses coordonnées cartésiennes dans le plan """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __del__(self):
        print("Point détruit")


class Rectangle:
    """ Rectangle défini par largeur, hauteur et position du point supérieur gauche """

    def __init__(self, largeur=0, hauteur=0, coin=Point()):
        self._largeur = largeur
        self._hauteur = hauteur
        self.coin = coin

    def __repr__(self):
        return 'L: ' + str(self._largeur) + ', H: ' + str(self._hauteur) + ', Coin: ' + str(self.coin)

    def __del__(self):
        print("Rectangle détruit")

    @property
    def largeur(self):
        return self._largeur

    @property
    def hauteur(self):
        return self._hauteur

    @largeur.setter
    def largeur(self, valeur):
        # On s'assure que la valeur est réelle et positive
        if isinstance(valeur, (int, float)) and (valeur >= 0):
            self._largeur = valeur

    @hauteur.setter
    def hauteur(self, valeur):
        # On s'assure que la valeur est réelle et positive
        if isinstance(valeur, float) and (valeur >= 0):
            self._hauteur = valeur


def trouve_centre(rectangle):
    centre = Point(rectangle.coin.x + rectangle.largeur / 2.,
                   rectangle.coin.y - rectangle.hauteur / 2.)
    return centre


i = Point(1, 0)
print('test point : ', i)

coin_superieur_gauche = Point(2, 10)

mon_rectangle = Rectangle(4, 6, coin_superieur_gauche)
print(mon_rectangle)

mon_rectangle.largeur = 10
print(mon_rectangle)
mon_rectangle.hauteur = mon_rectangle.hauteur - 20  # Modification non effectuée car < 0
print(mon_rectangle)

centre_de_mon_rectangle = trouve_centre(mon_rectangle)
print('type(centre_de_mon_rectangle) =', type(centre_de_mon_rectangle))
print('centre_de_mon_rectangle : ', centre_de_mon_rectangle)
