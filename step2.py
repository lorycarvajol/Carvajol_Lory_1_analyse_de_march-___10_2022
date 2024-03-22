import requests
from bs4 import BeautifulSoup
import csv

# URL de la page à scraper
url = "http://books.toscrape.com/catalogue/category/books/romance_8/index.html"

# Envoi d'une requête HTTP à l'URL spécifiée et analyse du contenu HTML avec BeautifulSoup
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


# Fonction pour récupérer tous les liens des pages contenant les livres
def get_all_pages(url):
    # Envoi d'une requête HTTP à l'URL spécifiée et analyse du contenu HTML avec BeautifulSoup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Recherche de tous les livres sur la page
    books = soup.find_all("h3")
    for book in books:
        # Récupération du lien du livre et ajustement de l'URL
        link = book.find("a")["href"]
        link = link.replace("../../../", "http://books.toscrape.com/catalogue/")
        yield link

    # Recherche du lien vers la page suivante s'il existe
    next_page = soup.find("li", class_="next")
    if next_page:
        next_page = next_page.find("a")["href"]
        next_page = next_page.replace("index.html", "")
        next_page = url.replace("index.html", next_page)
        # Appel récursif pour récupérer les liens des pages suivantes
        yield from get_all_pages(next_page)


# Fonction pour extraire les informations d'un livre à partir de son URL
def get_book_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Extraction des informations spécifiques du livre
    title = soup.find("h1").text
    price = soup.find("p", class_="price_color").text
    stock = soup.find("p", class_="instock availability").text.strip()
    stock = stock.strip("In stock (").split()[0]
    stock = int(stock)
    description = soup.find("div", id="product_description").find_next_sibling("p").text
    category = soup.find("ul", class_="breadcrumb").find_all("li")[2].text
    upc = soup.find("td").text
    rating = soup.find("p", class_="star-rating")["class"][1]
    rating = int(
        rating.replace("One", "1")
        .replace("Two", "2")
        .replace("Three", "3")
        .replace("Four", "4")
        .replace("Five", "5")
    )
    image = soup.find("img")["src"]
    image = image.replace("../../", "http://books.toscrape.com/")

    # Retourne les informations extraites sous forme de dictionnaire
    return {
        "product_page_url": url,
        "universal_product_code": upc,
        "title": title,
        "price_including_tax": price,
        "price_excluding_tax": price,
        "number_available": stock,
        "product_description": description,
        "category": category,
        "review_rating": rating,
        "image_url": image,
    }


# Ouverture du fichier CSV en mode écriture avec encodage UTF-8
with open("romance.csv", "w", encoding="utf-8-sig", newline="") as csvfile:
    # Définition des noms de colonnes
    fieldnames = [
        "product_page_url",
        "universal_product_code",
        "title",
        "price_including_tax",
        "price_excluding_tax",
        "number_available",
        "product_description",
        "category",
        "review_rating",
        "image_url",
    ]
    # Création du writer pour écrire dans le fichier CSV
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # Écriture de l'en-tête du fichier CSV
    writer.writeheader()
    # Boucle sur tous les liens des pages contenant les livres et écriture des informations dans le fichier CSV
    for link in get_all_pages(url):
        writer.writerow(get_book_info(link))
