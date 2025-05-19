
# 🧠 Projet Programmation Orientée Objet (POO)


## Mini monde : simulation économique très simplifiée

### Énoncé :

Un simulateur fait "vivre" trois personnages économiques que sont :
1. Le Paysan
2. Le Meunier
3. Le Boulanger

Les classes à construire sont :
1. Le Paysan
. Mange du pain pour vivre
. Produit du blé
. Livre du blé à un meunier
. Reçoit du pain

2. Le Meunier
. Mange du pain pour vivre
. Reçoit du blé
. Produit de la farine en consommant du blé
. Livre de la farine à un boulanger
. Reçoit du pain

3. Le Boulanger
. Mange du pain (de son propre stock) pour vivre
. Reçoit de la farine
. Fabrique du pain en consommant de la farine
. Livre du pain aux meuniers et aux paysans (en fait, à tous ceux qui peuvent en recevoir)

Etablir les trois "identités de classe" des personnages, en décrivant les attributs nécessaires.

Peut-on trouver un principe "plus abstrait" qui permette de factoriser certains éléments ?
Etablir cette classe.

Identifier les comportements communs et les résoudre dans cette classe.

Modifier et terminer les classes personnages pour tenir compte de cette factorisation.


Evaluer une manière "intéressante" de procéder aux échanges de matière.

Ecrire une petite classe "enveloppante" qui mette en scène trois personnages et les fassent
"vivre" dans une boucle en mode "tour par tour".

➡️ Exemple de code pour commencer :
```python
# Micro-monde économique de la boulangerie
# Pas d'utilisation des décorateurs pour définir les classes
# et méthodes abstraites


class Produit:  # Classe abstraite
    def __init__(self):
        self.quantite = 0
        self._type = 'Produit non défini'  # Attribut protégé

    def __repr__(self):
        # >>> Début de votre code
        pass
        #     Fin de votre code <<<


class Pain(Produit):
    def __init__(self, quantite):
        # >>> Début de votre code
        pass
        #     Fin de votre code <<<


class Personnage:  # Classe abstraite
    def __init__(self):
        # Chaque personnage commence le jeu avec 2 pains
        # >>> Début de votre code
        pass
        #     Fin de votre code <<<

    def manger(self):
        """
        Renvoie:
        Vrai si le personnage a reussi à manger
        Faux si personnage n'a pas pu manger
        """
        # >>> Début de votre code
        pass
        #     Fin de votre code <<<


class Paysan(Personnage):
    pass

    # ### Programme Principal ### #
# pain = Pain(2)
# print(pain)


paysan = Paysan()
# Faire manger le paysan tant qu'il y a du pain
# J'ai bien mangé
# Pain restant :  1
# J'ai bien mangé
# Pain restant :  0
# J'ai faim

```
---