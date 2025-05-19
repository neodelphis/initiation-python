
# 📚 Exercices du Chapitre 1 – Le hasard

## 🔢 Exercice 1.1
### Énoncé :
1. Écrivez un programme qui simule le jet de trois dés à six faces (on additionne le résultat des trois dés).
2. Écrivez un programme qui simule 50 jets de trois dés à six faces.
3. Écrivez un programme qui simule 200 jets de deux dés à huit faces.

### ✅ Solution proposée :

```python
from random import randint

# 1. Un seul jet de 3 dés à 6 faces
jet = randint(1, 6) + randint(1, 6) + randint(1, 6)
print("Résultat d’un jet de 3 dés :", jet)

# 2. 50 jets de 3 dés à 6 faces
for _ in range(50):
    total = randint(1, 6) + randint(1, 6) + randint(1, 6)
    print(total, end=" ")

# 3. 200 jets de 2 dés à 8 faces
for _ in range(200):
    total = randint(1, 8) + randint(1, 8)
    print(total, end=" ")
```

---

## 🔢 Exercice 1.2
### Énoncé :
Trouvez un moyen de simuler un dé pipé à six faces :
- 1 apparaît dans 10 % des cas,
- 2, 3, 4 et 5 dans 15 % des cas,
- 6 dans 30 % des cas.

Écrivez un programme qui simule 100 jets de ce dé.

### ✅ Solution proposée :

```python
from random import random

resultats = []

for _ in range(100):
    r = random()
    if r < 0.1:
        resultats.append(1)
    elif r < 0.25:
        resultats.append(2)
    elif r < 0.4:
        resultats.append(3)
    elif r < 0.55:
        resultats.append(4)
    elif r < 0.7:
        resultats.append(5)
    else:
        resultats.append(6)

print("Premiers résultats :", resultats[:10])
```

---

## 🔢 Exercice 1.3
### Énoncé :
Écrivez un programme qui génère un mot de passe de 8 caractères aléatoires, choisis parmi les 26 lettres minuscules et les 10 chiffres.

### ✅ Solution proposée :

```python
from random import choice
import string

def generer_mdp(longueur=8):
    caracteres = string.ascii_lowercase + string.digits
    return ''.join(choice(caracteres) for _ in range(longueur))

print("Mot de passe généré :", generer_mdp())
```

---

## 🔢 Exercice 1.4
### Énoncé :
Le Royal Rumble est une bataille royale exposant 30 catcheurs durant un combat. Écrivez un programme qui donnera un ordre d'entrée aléatoire des catcheurs.

Liste des catcheurs :
```
Wade Barrett, Daniel Bryan, Sin Cara, John Cena, Antonio Cesaro, Brodus Clay,
Bo Dallas, The Godfather, Goldust, Kane, The Great Khali, Chris Jericho,
Kofi Kingston, Jinder Mahal, Santino Marella, Drew McIntyre, The Miz,
Rey Mysterio, Titus O'Neil, Randy Orton, David Otunga, Cody Rhodes, Ryback,
Zack Ryder, Damien Sandow, Heath Slater, Sheamus, Tensai, Darren Young,
Dolph Ziggler
```

### ✅ Solution proposée :

```python
from random import shuffle

catcheurs = [
    "Wade Barrett", "Daniel Bryan", "Sin Cara", "John Cena", "Antonio Cesaro",
    "Brodus Clay", "Bo Dallas", "The Godfather", "Goldust", "Kane",
    "The Great Khali", "Chris Jericho", "Kofi Kingston", "Jinder Mahal",
    "Santino Marella", "Drew McIntyre", "The Miz", "Rey Mysterio",
    "Titus O'Neil", "Randy Orton", "David Otunga", "Cody Rhodes", "Ryback",
    "Zack Ryder", "Damien Sandow", "Heath Slater", "Sheamus", "Tensai",
    "Darren Young", "Dolph Ziggler"
]

shuffle(catcheurs)

print("Ordre d'entrée au Royal Rumble :")
for i, catcheur in enumerate(catcheurs, start=1):
    print(f"{i}. {catcheur}")
```

---

## 🔢 Exercice 1.5
### Énoncé :
Écrivez un programme qui simule un tirage Euro Millions : cinq numéros tirés au sort entre 1 et 50, suivis de deux étoiles numérotées de 1 à 12.

Exemple :
```
Numéros : [12, 24, 35, 41, 49]
Étoiles : [3, 9]
```

### ✅ Solution proposée :

```python
from random import sample

numeros = sample(range(1, 51), 5)
etoiles = sample(range(1, 13), 2)

print("Numéros :", numeros)
print("Étoiles :", etoiles)
```

---

## 🔢 Exercice 1.6
### Énoncé :
Simulez une partie de bingo. Les boules sont numérotées de 1 à 90. Il faut mélanger les boules.

### ✅ Solution proposée :

```python
from random import shuffle

boules = list(range(1, 91))
shuffle(boules)

print("Ordre des boules tirées au bingo :")
for i, numero in enumerate(boules, start=1):
    print(f"{i} → {numero}")
```

---

## 🔢 Exercice 1.7
### Énoncé :
Simulez 100 jets d'une pièce truquée qui montre "face" dans 57,83 % des cas.

### ✅ Solution proposée :

```python
from random import random

faces = 0
piles = 0

for _ in range(100):
    r = random()
    if r < 0.5783:
        faces += 1
    else:
        piles += 1

print(f"Face est apparu {faces} fois sur 100.")
print(f"Pile est apparu {piles} fois sur 100.")
```

---

## 🔢 Exercice 1.8
### Énoncé :
Dans le jeu Hearthstone, les proportions de raretés des cartes sont :
- 1 % légendaires (L),
- 4 % épiques (E),
- 23 % rares (R),
- 72 % communes (C).

Générez un paquet de 5 cartes tirées au sort en respectant ces proportions. Si un paquet ne contient que des communes, indiquez qu’il n’est pas valide.

### ✅ Solution proposée :

```python
from random import random

def generer_carte():
    r = random()
    if r < 0.01:
        return 'L'
    elif r < 0.05:
        return 'E'
    elif r < 0.28:
        return 'R'
    else:
        return 'C'

def generer_paquet():
    paquet = [generer_carte() for _ in range(5)]
    if 'L' in paquet or 'E' in paquet or 'R' in paquet:
        return paquet
    else:
        return None

paquets_valides = []
paquets_invalides = 0

while len(paquets_valides) < 10:  # Générer 10 paquets valides
    p = generer_paquet()
    if p:
        paquets_valides.append(p)
    else:
        paquets_invalides += 1

print("Paquets valides :")
for idx, paquet in enumerate(paquets_valides, 1):
    print(f"{idx} : {paquet}")

print(f"\nNombre de paquets invalides générés : {paquets_invalides}")
```

---

## 🔢 Exercice 1.9
### Énoncé :
Les cinq solides platoniciens peuvent être utilisés comme dés réguliers :
- tétraèdre (4 faces),
- cube (6 faces),
- octaèdre (8 faces),
- dodécaèdre (12 faces),
- icosaèdre (20 faces).

Procédure :
1. Lancer le tétraèdre pour choisir l’un des quatre autres dés à utiliser.
2. Lancer ce dé et noter le résultat.

Générez 100 nombres aléatoires selon ce protocole.

### ✅ Solution proposée :

```python
from random import randint

des = [6, 8, 12, 20]  # Faces des dés après avoir lancé le tétraèdre (sauf lui-même)

resultats = []

for _ in range(100):
    choix_de = randint(0, 3)  # Choisir l'un des 4 dés
    faces = des[choix_de]
    resultat = randint(1, faces)
    resultats.append(resultat)

print("Résultats des 100 lancers :", resultats)
```

---
