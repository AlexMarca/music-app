# Music App Project

## Description
Music App est une application web construite avec **Flask** qui permet de travailler la musique à travers des exercices quotidiens. L'application affiche des partitions musicales pour que l'utilisateur puisse s'exercer, et inclut une page de paramètres pour personnaliser l'expérience.

## Fonctionnalités actuelles
- **Page d'accueil (Menu principal)** : Affiche deux options principales : "Lancer un exercice" et "Paramètres".
- **Page d'exercice** : Affichage d'une partition musicale pour l'exercice du jour.
- **Page des paramètres** : Affiche un message simple "Page des paramètres" (à développer).

## Structure du projet

music-app/ # Dossier principal du projet ├── app.py # Serveur Flask principal qui gère les routes ├── templates/ # Dossier contenant les fichiers HTML │ ├── index.html # Page d'accueil (Menu principal) │ ├── exercice.html # Page d'exercice musical │ ├── parametres.html # Page des paramètres ├── static/ # Dossier pour les fichiers statiques (CSS, images, etc.) │ ├── css/ # Dossier contenant les fichiers CSS │ │ ├── style.css # Fichier CSS pour le style de l'application


## Technologies utilisées
- **Flask** : Framework web pour Python.
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
### 3. Lancer l'application
Lance le serveur Flask avec la commande suivante :

```bash
python app.py
```

L'application sera disponible sur http://127.0.0.1:5000/.

## Fonctionnalités à ajouter
Suivi de la progression : Ajouter un système pour suivre les exercices réalisés par l'utilisateur.

Personnalisation des exercices : Adapter les exercices en fonction du niveau de l'utilisateur.

Générateur de partitions musicales : Générer automatiquement des partitions pour chaque exercice.

Sauvegarde des préférences : Permettre aux utilisateurs de sauvegarder leurs paramètres et préférences.