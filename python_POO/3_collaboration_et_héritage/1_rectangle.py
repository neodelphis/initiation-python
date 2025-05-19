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
