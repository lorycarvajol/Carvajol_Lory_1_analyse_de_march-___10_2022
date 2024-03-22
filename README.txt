# Projet de Scraping de Livres

Ce projet vise à extraire des informations sur les livres à partir du site "http://books.toscrape.com" en utilisant Python et BeautifulSoup pour le scraping web.

## Description

Le script principal (`main.py`) parcourt différentes catégories de livres sur le site web, extrait les détails de chaque livre (titre, prix, disponibilité, description, etc.) et les stocke dans des fichiers CSV séparés pour chaque catégorie.

## Installation

1. Clonez ce dépôt vers votre machine locale :


2. Assurez-vous d'avoir Python 3 installé sur votre machine.


3. Installez les dépendances en exécutant la commande suivante dans votre terminal :

pip install -r requirements.txt

## Utilisation

1. Exécutez le script `main.py` pour lancer le scraping :

python main.py


2. Les données seront extraites et stockées dans des fichiers CSV dans le répertoire `categories`.

## Structure du Projet

- `main.py` : le script principal pour lancer le scraping.
- `scraping.py` : les fonctions pour effectuer le scraping des données.
- `categories/` : répertoire contenant les fichiers CSV pour chaque catégorie de livres.

## Auteur

[lorycarvajol](https://github.com/votre-utilisateur)

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.
