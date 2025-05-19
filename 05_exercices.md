
# 🧩 Fonctions, modules et fichiers

## 🧠 Objectif pédagogique
Renforcer la compréhension des concepts suivants :
- Création de fonctions réutilisables
- Utilisation des modules Python
- Gestion des chemins et fichiers
- Programmation fonctionnelle légère (avec lambda)
- Organisation en scripts autonomes

---

# 📌 Exercice 1 : Générateur de mots de passe sécurisé

### Énoncé :

Écris un programme qui génère **un mot de passe sécurisé** contenant :
- Au moins une majuscule
- Au moins une minuscule
- Au moins un chiffre
- Au moins un caractère spécial
- Une longueur minimum de 12 caractères

Le mot de passe doit être généré **aléatoirement**, et le programme doit **vérifier qu’il est valide** avant de le retourner.

💡 Utilise les modules :
- `random`
- `string`

---

# 📌 Exercice 2 : Analyse d’un fichier texte

### Énoncé :

Crée un programme qui analyse un fichier texte (`texte.txt`) et affiche :
- Le nombre total de mots
- Le mot le plus fréquent
- La moyenne de lettres par mot
- Les lignes contenant un mot clé donné (ex. `'erreur'`)

💡 Utilise :
- `collections.Counter`
- `string.punctuation`
- Des fonctions bien organisées

---

# 📌 Exercice 3 : Renommeur de fichiers en masse

### Énoncé :

Écris un script qui renomme tous les fichiers d’un dossier selon un motif donné.

Exemple :
```bash
photo_001.jpg
photo_002.jpg
...
```

Le programme devra :
- Prendre en argument le dossier et le préfixe
- Renommer les fichiers avec un numéro incrémenté
- Ignorer les fichiers cachés ou systèmes

💡 Utilise :
- `os.listdir()`
- `os.rename()`
- `sys.argv` pour passer les arguments

---

# 📌 Exercice 4 : Calculateur d’âge précis

### Énoncé :

Écris une fonction qui prend une date de naissance au format `'YYYY-MM-DD'` et retourne l’âge actuel de la personne en années, mois et jours.

Exemple :
```python
calculer_age('1995-06-15') → {'années': 29, 'mois': 3, 'jours': 12}
```

💡 Utilise :
- `datetime`
- `.today()` et soustraction de dates via `timedelta`

---

# 📌 Exercice 5 : Mini-script CLI avec `sys.argv`

### Énoncé :

Crée un petit outil en ligne de commande qui accepte des arguments comme suit :

```bash
python outils.py --help
python outils.py --upper "bonjour"
python outils.py --lower "BONJOUR"
python outils.py --count "mot"
```

Exemples :
- `--upper` : convertit en majuscules
- `--lower` : convertit en minuscules
- `--count` : compte le nombre de lettres

💡 Utilise :
- `sys.argv`
- Des fonctions bien séparées
- Un système de gestion d’aide (`--help`)

---

# 📌 Exercice 6 : Horloge de bureau améliorée

### Énoncé :

Écris un programme qui affiche l’heure courante dans un format personnalisé, avec :
- L’affichage mis à jour toutes les secondes
- Affichage du fuseau horaire local
- Indication si c’est le week-end ou un jour férié (optionnel)

💡 Utilise :
- `datetime`
- Boucle infinie + `time.sleep(1)`
- Optionnel : module `holidays` ou liste manuelle de jours fériés

---

# 📌 Exercice 7 : Nettoyeur de dossier temporaire

### Énoncé :

Écris un script qui nettoie automatiquement un dossier en supprimant les fichiers créés il y a plus de X jours (paramétrable).

Le script devra :
- Accepter le chemin du dossier et l’âge limite en jours comme arguments
- Ne pas supprimer les dossiers imbriqués
- Être sûr (ne pas supprimer par erreur)

💡 Utilise :
- `os.listdir()`, `os.path.getmtime()`
- `time.time()`
- `os.remove()`

