## 🧠 Objectif des exercices

- Comparer les structures Python avec celles d'autres langages (Java, C++, JS…)
- Manipuler plusieurs structures ensemble
- Pratiquer l’algorithmie basique
- Apprendre à choisir la bonne structure selon le besoin

---

## 📌 Exercice 1 : Fusion et nettoyage de listes

### Énoncé :
Tu as deux listes de nombres. Tu dois :
1. Concaténer les deux listes.
2. Supprimer les doublons.
3. Trier le résultat dans l’ordre croissant.
4. Retourner uniquement les nombres pairs.

```python
liste1 = [3, 7, 10, 15, 2]
liste2 = [5, 10, 20, 3]

# Ton code ici
```

### Résultat attendu :
```python
[2, 10, 20]
```

---

## 📌 Exercice 2 : Statistiques sur un texte

### Énoncé :
Écris un programme qui analyse un texte et affiche :
- Le nombre total de mots
- Le mot le plus fréquent
- La longueur moyenne des mots

Utilise un dictionnaire pour compter les occurrences.

```python
texte = "le chat noir est dans le jardin et le chien regarde le chat"
```

💡 Astuce : Utilise `.split()` pour découper le texte.

---

## 📌 Exercice 3 : Recherche dans une base de données simplifiée

### Énoncé :
Crée une liste de dictionnaires représentant des étudiants :

```python
etudiants = [
    {'nom': 'Alice', 'âge': 22, 'notes': {'math': 18, 'français': 16}},
    {'nom': 'Bob', 'âge': 20, 'notes': {'math': 14, 'français': 19}},
    {'nom': 'Charlie', 'âge': 21, 'notes': {'math': 15, 'français': 17}}
]
```

#### Partie 1 :
Trouve tous les étudiants dont la note en math est supérieure ou égale à 15.

#### Partie 2 (facultatif) :
Calcule la moyenne générale de chaque étudiant et ajoute-la dans un nouveau champ `'moyenne'`.

---

## 📌 Exercice 4 : Gestion de contacts (dictionnaire imbriqué)

### Énoncé :
Crée un dictionnaire `annuaire` où :
- La clé est le nom d’une personne
- La valeur est un autre dictionnaire contenant :
  - `'téléphone'`
  - `'email'`
  - `'adresse'`

Exemple :

```python
annuaire = {
    'Jean Dupont': {
        'téléphone': '06 12 34 56 78',
        'email': 'jean.dupont@email.com',
        'adresse': '12 rue des Champs'
    },
    # ...
}
```

Ajoute une fonction `chercher_contact(nom)` qui affiche les informations si le contact existe, sinon affiche un message d’erreur.

---

## 📌 Exercice 5 : Jeu du Mastermind simplifié

### Énoncé :
Implémente une version très simplifiée du jeu du Mastermind :

- Une combinaison secrète de 4 couleurs parmi : `'rouge'`, `'bleu'`, `'vert'`, `'jaune'`, `'orange'`, `'violet'`
- Le joueur a 10 tentatives
- À chaque tentative, affiche :
  - Nombre de couleurs correctes ET bien placées
  - Nombre de couleurs correctes MAIS mal placées

💡 Utilise des listes et des ensembles pour faciliter les comparaisons.

---

## 📌 Exercice 6 : Optimisation de recherche dans une liste

### Énoncé :
On te donne une grande liste de noms (plusieurs milliers). Tu dois comparer la performance entre :

1. Vérifier si un nom est dans la liste (`in list`)
2. Vérifier si un nom est dans un ensemble (`in set`)

Utilise le module `time` pour mesurer le temps pris par chaque opération.

👉 Conclusion attendue : les ensembles sont beaucoup plus rapides que les listes pour les recherches.

---

## 📌 Exercice 7 : Tri personnalisé de tuples

### Énoncé :
Voici une liste de tuples représentant des personnes :

```python
personnes = [
    ('Alice', 25),
    ('Bob', 20),
    ('Claire', 30),
    ('David', 20)
]
```

Trie cette liste :
1. Par ordre alphabétique du nom
2. Puis par âge croissant

💡 Utilise `sorted()` avec un `key` personnalisé.

---

## 📌 Exercice 8 : Compteur de bigrammes dans un texte

### Énoncé :
Un *bigramme* est une paire de mots successifs dans un texte.  
Exemple : dans `"le chat noir"`, les bigrammes sont `('le', 'chat')`, `('chat', 'noir')`.

Compte les bigrammes présents dans un texte donné et affiche les 5 les plus fréquents.

```python
texte = "le chat dort le chat ronronne"
```

💡 Utilise une liste de mots et itère dessus pour créer les paires. Stocke les résultats dans un dictionnaire.