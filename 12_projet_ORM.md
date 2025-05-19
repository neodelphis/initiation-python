
## 🎮 Projet Éducatif : "Gestion d'un Club de Jeux Vidéo"

### 📌 Objectif pédagogique
Permettre aux étudiants de découvrir **SQLAlchemy (Core et ORM)** avec Python, en implémentant une petite application de gestion pour un club de jeux vidéo.  
Ils apprendront à créer des modèles, interagir avec une base SQLite, effectuer des requêtes simples et complexes, et structurer leur code.

---

## 🧩 Énoncé du projet

Vous êtes chargé de développer une application qui permet de gérer les membres, les tournois et les jeux vidéo d’un club étudiant passionné de jeux vidéo.

### 💡 Fonctionnalités attendues :
1. Gérer les joueurs (nom, pseudo, date d’inscription)
2. Gérer les jeux (titre, genre, date de sortie)
3. Organiser des tournois (jeu, date, organisateur)
4. Inscrire des joueurs à des tournois
5. Afficher les résultats (optionnel)

---

## 🗂️ Structure de départ proposée

Voici une structure de code de base utilisant **SQLAlchemy ORM** avec une base **SQLite** :

### 1. `models.py` – Définition des modèles

```python
# models.py
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Joueur(Base):
    __tablename__ = 'joueurs'
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    pseudo = Column(String, unique=True)
    date_inscription = Column(Date)
    
    tournois = relationship("Tournoi", secondary="participations", back_populates="participants")

class Jeu(Base):
    __tablename__ = 'jeux'
    id = Column(Integer, primary_key=True)
    titre = Column(String, unique=True)
    genre = Column(String)
    date_sortie = Column(Date)

    tournois = relationship("Tournoi", back_populates="jeu")

class Tournoi(Base):
    __tablename__ = 'tournois'
    id = Column(Integer, primary_key=True)
    jeu_id = Column(Integer, ForeignKey('jeux.id'))
    date = Column(Date)
    organisateur = Column(String)

    jeu = relationship("Jeu", back_populates="tournois")
    participants = relationship("Joueur", secondary="participations", back_populates="tournois")

class Participation(Base):
    __tablename__ = 'participations'
    joueur_id = Column(Integer, ForeignKey('joueurs.id'), primary_key=True)
    tournoi_id = Column(Integer, ForeignKey('tournois.id'), primary_key=True)

# Connexion à la base SQLite
engine = create_engine('sqlite:///club_jeux.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
```

---

### 2. `main.py` – Exemple d’utilisation

```python
# main.py
from models import session, Joueur, Jeu, Tournoi

# Ajouter quelques données
joueur1 = Joueur(nom="Alice Dupont", pseudo="Alicia", date_inscription="2024-01-15")
joueur2 = Joueur(nom="Bob Martin", pseudo="Bobby", date_inscription="2024-02-01")

jeu1 = Jeu(titre="Super Smash Bros", genre="Combat", date_sortie="2018-12-07")
jeu2 = Jeu(titre="Minecraft", genre="Sandbox", date_sortie="2011-11-18")

tournoi1 = Tournoi(jeu=jeu1, date="2024-06-10", organisateur="Club Game")
tournoi1.participants.append(joueur1)
tournoi1.participants.append(joueur2)

# Sauvegarder dans la base
session.add_all([joueur1, joueur2, jeu1, jeu2, tournoi1])
session.commit()

# Requête simple : afficher tous les joueurs
print("Liste des joueurs :")
for j in session.query(Joueur).all():
    print(f"- {j.pseudo} ({j.nom})")

# Requête plus complexe : afficher les tournois avec leurs jeux
print("\nTournois organisés :")
for t in session.query(Tournoi).all():
    print(f"- {t.jeu.titre} le {t.date}, organisé par {t.organisateur}")
    print("  Participants :")
    for p in t.participants:
        print(f"   - {p.pseudo}")
```

---

## 🛠️ Instructions pour les étudiants

1. Créer l’environnement virtuel conda `orm` et installer SQLAlchemy :
   ```bash
    conda activate orm
    conda install conda-forge::sqlalchemy
   ```

2. Exécuter le script principal :
   ```bash
   python main.py
   ```
   Cela va créer la base SQLite (`club_jeux.db`) et y ajouter quelques données.

3. Avec [DBeaver](https://dbeaver.io/) ou autre créer le diagramme de la base de données

4. Installer la bibliothèque Faker pour générer des profils d'étudiants
```python
from faker import Faker
fake = Faker(['fr_FR']) # Pour avoir des exemples en français

Créez quelques entrées avec ce module pour les joueurs et les jeux.
```

5. Explorer les fonctionnalités :
   - Ajouter des méthodes utilitaires (ex: inscrire un joueur à un tournoi)
   - (bonus) Implémenter une interface en ligne de commande (CLI) pour gérer les objets 
   - Permettre la modification/suppression d'éléments

6. Système de score et podiums
    - Ajouter des scores
    - Podium et classements dans un tournois

7. Faire évoluer le modèle pour gérer plusieurs club.
L'organisateur d'un tournoi doit être un des clubs existants.
---

## 🔍 Concepts abordés

- Utilisation de l’ORM SQLAlchemy
- Relations entre tables (One-to-many, Many-to-many)
- Sessions et transactions
- Requêtes simples et jointures
- Bonnes pratiques de structuration du code

---

## 🚀 Idées d’évolutions possibles
Les étoiles indiquent le niveau de difficulté.

- (*) Export CSV des participants
- (*) Système de score et podiums
- (***) Interface graphique (Tkinter, PyQt ou Flask)
- (**) Authentification pour les administrateurs du club

