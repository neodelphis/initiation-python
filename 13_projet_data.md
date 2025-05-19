# 🧑‍💻 Projet : Analyseur de Données de Ventes

## 🎯 Objectif du projet :
Créer un programme Python qui permet d’analyser un fichier CSV contenant des données de ventes, et afficher des statistiques utiles telles que :

- Le chiffre d'affaires total
- Les produits les plus vendus
- La répartition par région
- etc.

---

## 📁 Énoncé

Tu as été embauché(e) comme développeur dans une entreprise commerciale. Ton rôle est de créer un outil d’analyse des ventes à partir d’un fichier CSV fourni par l’équipe comptable.

Le fichier `ventes.csv` contient les informations suivantes :

| Date       | Produit     | Quantité | Prix unitaire | Région |
|------------|-------------|----------|----------------|--------|
| 2024-01-01 | Chaise      | 10       | 50             | Nord   |
| ...        | ...         | ...      | ...            | ...    |

---

## 🛠️ Consignes Techniques

### 1. **Chargement des données**
Utilise la bibliothèque `pandas` pour charger les données du fichier CSV dans un DataFrame.

🔧 Astuce : Tu devras probablement faire des conversions de type.

---

### 2. **Nettoyage des données**

Utilise la fonction `filter()` pour garder uniquement les ventes valides :

- La quantité doit être supérieure à 0.
- Le prix unitaire doit être supérieur à 0.

✅ **Questions :**
1. Quel type de lambda peux-tu utiliser avec `filter()` pour effectuer ce nettoyage ?
2. Comment gères-tu les valeurs manquantes ou incorrectes éventuelles ?

---

### 3. **Transformation des données**

Utilise la fonction `map()` pour enrichir les données :

- Convertir `'Quantité'` et `'Prix unitaire'` en entiers.
- Ajouter un nouveau champ `'Montant total' = Quantité × Prix unitaire`.

---

### 4. **Calculs Statistiques**

Implémente les fonctions suivantes :

- ✅ Calcul du **chiffre d’affaires total**.
- ✅ Trouver la **meilleure vente** (celle avec le plus grand montant).
- ✅ Calcul de la **moyenne des montants**.
- ✅ Top 5 des **produits les plus vendus** (en quantité totale).
- ✅ Répartition des ventes par **région** (total de ventes ou montant total par région).

✅ **Questions :**
6. Quelle structure de données utiliserais-tu pour stocker les totaux par région ?
7. Peux-tu utiliser `collections.Counter` pour compter les ventes par produit ?
8. Comment trier les produits du plus vendu au moins vendu ?
9. Comment afficher joliment les résultats dans la console (formattage, alignement...) ?

---

### 5. **Options avancées (optionnel)**

🔍 Si tu veux aller plus loin :
1. Trie les résultats et affiche seulement les 5 premiers.
2. Exporte les résultats dans un fichier texte (`rapport.txt`) ou un nouveau CSV.
3. Affiche un graphique simple (par exemple, bar chart des ventes par région).

---

## 📝 Fichier CSV d'exemple

Un fichier `ventes.csv` est fourni avec environ 50 lignes de ventes de trois produits : chaises, tables et lampes, répartis sur 15 jours, dans différentes régions.

---

## 💡 Conseils Généraux

- Structure ton code en plusieurs fonctions claires : chargement, nettoyage, calculs, affichage, export.
- Teste souvent chacune des étapes pour éviter les erreurs silencieuses.
- Utilise des commentaires ou docstrings pour expliquer ton code.
- Si tu travailles en groupe, divisez les tâches !

---

## 🧪 Suggestions de tests

Voici quelques petits tests que tu peux faire pour valider ton code :

```python
# Exemple de test pour vérifier le filtre
vente_test = {"Quantité": "0", "Prix unitaire": "50"}
assert not est_vente_valide(vente_test), "La vente devrait être rejetée car la quantité est nulle"

# Exemple de test pour le calcul du montant total
vente_test = {"Quantité": "2", "Prix unitaire": "100"}
assert calculer_montant_total(vente_test) == 200, "Le montant devrait être 200"
```

---
## 📁 Structure du projet suggérée :

```
analyse_ventes/
│
├── data/
│   └── ventes.csv
├── rapport/
│   └── resultat.txt
├── main.py
└── utils.py  # fonctions utilitaires
```

---
