# Music App Project

## Description
Music App est une application web construite avec **Flask** qui permet de travailler la musique à travers des exercices quotidiens. L'application affiche des partitions musicales pour que l'utilisateur puisse s'exercer, et inclut une page de paramètres pour personnaliser l'expérience.

## Fonctionnalités actuelles
- **Page d'accueil (Menu principal)** : Affiche deux options principales : "Lancer un exercice" et "Paramètres".
- **Page d'exercice** : Affichage d'une partition musicale pour l'exercice du jour.
- **Page des paramètres** : Affiche un message simple "Page des paramètres" (à développer).
- **Inscription et Connexion** :
  - Inscription via un formulaire avec nom d'utilisateur, email et mot de passe.
  - Connexion sécurisée avec gestion des sessions utilisateur.
  - Protection des pages nécessitant une authentification.
  - Déconnexion disponible.

## Structure du projet

music-app/ # Dossier principal du projet ├── app.py # Serveur Flask principal qui gère les routes et la base de données ├── instance/ # Contient la base de données SQLite (users.db) ├── templates/ # Dossier contenant les fichiers HTML │ ├── index.html # Page d'accueil (Menu principal) │ ├── exercice.html # Page d'exercice musical │ ├── parametres.html # Page des paramètres │ ├── login.html # Page de connexion │ ├── signup.html # Page d'inscription ├── static/ # Dossier pour les fichiers statiques (CSS, images, etc.) │ ├── css/ │ │ ├── style.css # Fichier CSS pour le style de l'application ├── requirements.txt # Liste des dépendances Python ├── README.md # Documentation du projet

markdown
Copier
Modifier

## Technologies utilisées
- **Flask** : Framework web pour Python.
- **Flask-Login** : Gestion des utilisateurs et authentification.
- **Flask-SQLAlchemy** : ORM pour gérer la base de données SQLite.
- **Werkzeug** : Sécurisation des mots de passe.
- **HTML/CSS** : Langages utilisés pour structurer et styliser les pages web.

## Instructions d'installation et d'exécution

### 1. Cloner le dépôt
Clone le projet depuis GitHub :

```bash
git clone https://github.com/ton_nom_utilisateur/music-app.git
```
### 2. Installer les dépendances
Crée un environnement virtuel et installe les dépendances nécessaires :

```bash
python -m venv venv  
source venv/bin/activate  # Sur Mac/Linux
venv\Scripts\activate     # Sur Windows
pip install -r requirements.txt
```
### 3. Initialiser la base de données
Avant de lancer l'application, initialise la base de données :

```bash
python -c "from app import db; db.create_all()"
```

### 4. Lancer l'application
Démarre le serveur Flask avec la commande suivante :

```bash
python app.py
```
L'application sera disponible sur http://127.0.0.1:5000/.

## Fonctionnalités à ajouter

Ajout de différent niveau d'authentification (admin, modérateur)

Restructuration du projet : 
music-app/                
├── app.py                 # Point d'entrée de l'application
├── config.py              # Configuration de l'application
├── routes/                # Dossier contenant les routes Flask
│   ├── __init__.py        # Fichier pour enregistrer les routes
│   ├── main_routes.py     # Routes pour la page d'accueil et navigation
│   ├── exercice_routes.py # Routes pour les exercices
│   ├── parametres_routes.py # Routes pour la page des paramètres
├── templates/             # Dossier contenant les fichiers HTML
│   ├── index.html         # Page d'accueil
│   ├── exercice.html      # Page d'exercice
│   ├── parametres.html    # Page des paramètres
├── static/                # Dossier pour les fichiers statiques (CSS, JS)
│   ├── css/               # Dossier contenant les styles CSS
│   │   ├── style.css      # Feuille de style principale
├── venv/                  # Environnement virtuel (ne pas versionner)
├── requirements.txt       # Liste des dépendances à installer
├── .gitignore             # Fichiers à ignorer par Git
└── README.md              # Documentation du projet
