

# 📚 Exercices du cours 3

## 🔢 Exercice 3.1

Écrivez un programme qui demande à l’utilisateur d’écrire des mots.  
Tant que l’utilisateur n’aura pas pressé sur la touche `Enter` toute seule, l’ordinateur demandera un nouveau mot.  
Le programme écrira ce mot, précédé de son numéro de rang.  
Poliment, l’ordinateur écrira « Au revoir » avant que le programme se termine.

---

## 🔢 Exercice 3.2

Ajoutez une boucle au programme suivant pour écrire les secondes.

```python
h = 0
while h < 24:
    m = 0
    while m < 60:
        print(h, "heure(s)", m, "minute(s)")
        m += 1
    h += 1
```

---

## 🔢 Exercice 3.3 – Partie 1

Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 53. Le résultat commencera comme ceci :

```
1 x 53 = 53
2 x 53 = 106
3 x 53 = 159
...
```

Aide : il existe une fonction de formatage qui permet d’aligner joliment les nombres en colonne du genre `{:2d}`

---

## 🔢 Exercice 3.3 – Partie 2

Modifiez la partie 1 pour obtenir un programme qui affiche toutes les tables de multiplication de 2 à 13. Chaque table comprendra 12 lignes. Alignez joliment les nombres dans les tables.

---

## 🔢 Exercice 3.4 – Livret

Écrivez un programme Python pour tester votre livret de tables de multiplications. Le programme demandera d’abord quel est le plus grand nombre (Nmax) qu’il pourra utiliser. Puis il proposera 10 questions de livret avec deux nombres tirés au sort dans l’intervalle [2, Nmax].

En cas de réponse erronée, le programme reposera la même question, tant que la bonne réponse n’aura pas été donnée.

---

## 🔢 Exercice 3.5 – Livret sous pression du temps

Améliorez le programme de l’exercice 3.4 : à la fin de la partie, affichez le nombre d’erreurs (avec la bonne orthographe) et le temps utilisé pour répondre aux dix questions.

Aide : dans le module `time`, se trouve la fonction `time()`, qui donne le nombre de secondes écoulées depuis le 1er janvier 1970 à 00:00:00.

---

## 🔢 Exercice 3.6 – Calcul mental

Améliorez le programme de l’exercice 3.5. Cette fois-ci, on ne veut pas se contenter d’exercer les multiplications, mais aussi l’addition, la soustraction et la division entière. L’opération à tester sera tirée au sort pour chaque question.

---

## 🔢 Exercice 3.7

Écrivez un programme qui simule 1000 lancers d’une pièce de monnaie. Vous afficherez seulement le nombre de piles et le nombre de faces obtenus.

Écrivez une version avec une boucle `for` (voir chapitre 1) et une autre avec une boucle `while`.

---

## 🔢 Exercice 3.8 – Les paquets de cartes Hearthstone

Améliorez le programme de l’exercice 1.8.

Générez `n` paquets de cartes Hearthstone valides.  
Comptez le nombre total de cartes de chaque rareté afin de vérifier que les pourcentages obtenus sont « proches » des pourcentages théoriques (plus vous générerez de paquets, plus les pourcentages seront proches de la théorie).

Exemple de sortie avec 10 paquets (50 cartes) :

```
R C R C C C R C C C C R C C L!
C R R C C C C C C C non valide C C C R C R C C C C E C E C C
2 légendaire(s): 4.00%
2 épique(s): 4.00%
12 rare(s): 24.00%
34 communes: 68.00%
```

Vous ajouterez un point d’exclamation après les paquets contenant au moins une légendaire.

---

## 🔢 Exercice 3.9

Modifiez le code du § 3.3 :

1. Avant de commencer le jeu, le programme demandera le prénom du joueur. Quand René trouvera le bon nombre, le programme le félicitera par la phrase :
   ```
   Bravo, René ! Vous avez trouvé 16 en 4 essai(s).
   ```

3. À la fin de la partie, le programme proposera une nouvelle partie au joueur, qui répondra par oui ou non. Quand le joueur arrêtera de jouer, le programme indiquera le pourcentage de réussite et le nombre moyen de tentatives pour trouver le nombre (on ne comptabilisera le nombre de coups qu’en cas de réussite).

---

## 🔢 Exercice 3.10

Inversons les rôles ! C’est l’ordinateur qui essaiera de deviner le nombre que vous avez en tête et vous lui indiquerez si le nombre qu’il proposera est trop petit ou trop grand.

Convention : entrez `1` si le nombre de l’ordinateur est trop grand, `2` s’il est trop petit et `0` si l’ordinateur a trouvé le bon nombre.

Prévoyez les cas où l’utilisateur écrit autre chose qu’une des trois réponses attendues.

---

## 🔢 Exercice 3.11 – Risk

Au jeu *Risk*, les combats se déroulent ainsi : l’assaillant désigne par leurs noms le territoire visé et le territoire attaquant.

L’assaillant prend trois dés de même couleur (rose). Il lance autant de dés qu’il engage d’armées (3 au maximum).  
Le défenseur, lui, ne peut lancer que 2 dés au maximum, même s’il a 3 armées ou plus sur son territoire.

On compare deux à deux les dés de plus haute valeur entre assaillant et défenseur. Puis si c'est possible les deux suivants.

Calculez à l’aide d’un programme et notez dans le tableau ci-après la probabilité de chacun des événements y figurant, en fonction du nombre de dés que chacun des deux joueurs choisit de lancer.

| | Nombre de dés lancés par le défenseur : 2 | Nombre de dés lancés par le défenseur : 1 |
|---|---|---|
| **Nombre de dés lancés par l'assaillant : 3** | L'assaillant perd 2 armées : ___ | L'assaillant perd 1 armée : ___ |
|  | Le défenseur perd 2 armées : ___ | e défenseur perd 1 armée : ___ |
|  | Chaque joueur perd 1 armée : ___ |  |
| **Nombre de dés lancés par l'assaillant : 2** | L'assaillant perd 2 armées : ___ | L'assaillant perd 1 armée : ___|
|   | Le défenseur perd 2 armées : ___ | Le défenseur perd 1 armée : ___ |
|   | Chaque joueur perd 1 armée : ___ |   |
| **Nombre de dés lancés par l'assaillant : 1** | L'assaillant perd 1 armée : ___ | L'assaillant perd 1 armée : ___ |
|   | Le défenseur perd 1 armée : ___ | Le défenseur perd 1 armée : ___ |




---

