# Project Title: Book Scraper from Books to Scrape

## Description

Ce projet est un scraper Python qui extrait les informations sur les livres à partir du site web fictif "Books to Scrape". Il récupère les détails tels que le titre du livre, le prix, la disponibilité en stock, la description du produit, la catégorie, le classement par étoiles, et l'URL de l'image de couverture. Les informations sont enregistrées dans des fichiers CSV organisés par catégories de livres, et les images de couverture sont téléchargées dans un dossier local.

## Features

- Extraction des URLs de tous les livres d'une catégorie donnée.
- Récupération et enregistrement des détails des livres dans des fichiers CSV.
- Téléchargement des images de couverture des livres.
- Gestion de la pagination pour les catégories contenant plusieurs pages de livres.
- Structure organisée des données récupérées, avec un dossier par catégorie.
- `.gitignore` configuré pour exclure les dossiers `categories/`, `images/`, et d'autres fichiers non nécessaires.

## Prerequisites

- Python 3.x
- Bibliothèques Python : `requests`, `BeautifulSoup4`, `csv`, `os`

## Installation

Clonez le dépôt GitHub :

git clone [https://github.com/lorycarvajol/Carvajol_Lory_1_analyse_de_march-___10_2022](https://github.com/lorycarvajol/Carvajol_Lory_1_analyse_de_march-___10_2022)

Installez les dépendances nécessaires :

pip install requests beautifulsoup4


## Usage

Pour exécuter le script de scraping, naviguez dans le dossier du projet cloné et lancez :

```
book_scraper.py
```


## Structure du Projet

- `book_scraper.py` : Script principal pour le scraping des livres.
- `categories/` : Dossier contenant les fichiers CSV organisés par catégories de livres (exclu par `.gitignore`).
- `images/` : Dossier contenant les images téléchargées des couvertures des livres (exclu par `.gitignore`).
- `.gitignore` : Fichier configuré pour exclure les dossiers `categories/`, `images/`, et d'autres fichiers non nécessaires.
- `README.md` : Ce fichier, expliquant le projet, son installation, et son utilisation.

## Contributing

Si vous souhaitez contribuer à ce projet, veuillez forker le dépôt et proposer des pull requests.


## Contact

  Lory Carvajol

Lien du projet : https://github.com/lorycarvajol/Carvajol_Lory_1_analyse_de_march-___10_2022
