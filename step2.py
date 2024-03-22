import requests
from bs4 import BeautifulSoup
import csv
import os


# Fonction pour extraire les informations d'un livre à partir de son URL
def get_book_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("h1").text
    price = soup.find("p", class_="price_color").text
    stock_text = soup.find("p", class_="instock availability").text.strip()
    # Extrait uniquement la partie numérique de la chaîne de stock
    stock = int("".join(filter(str.isdigit, stock_text)))
    description = soup.find("div", id="product_description")
    if description:
        description = description.find_next_sibling("p").text
    category = soup.find("ul", class_="breadcrumb").find_all("li")[2].text
    upc = soup.find("td").text
    rating = (
        soup.find("p", class_="star-rating")["class"][1]
        .replace("One", "1")
        .replace("Two", "2")
        .replace("Three", "3")
        .replace("Four", "4")
        .replace("Five", "5")
    )
    rating = int(rating)
    image = soup.find("img")["src"].replace("../../", "http://books.toscrape.com/")
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


# Fonction pour récupérer les URLs des livres d'une page d'une catégorie
def get_books_urls(category_url):
    page = requests.get(category_url)
    soup = BeautifulSoup(page.content, "html.parser")
    books_urls = []

    # Traitement de la première page
    books = soup.find_all("h3")
    for book in books:
        books_urls.append(
            "http://books.toscrape.com/catalogue/"
            + book.find("a")["href"].replace("../", "")
        )

    # Traitement des pages suivantes
    next_page = soup.find("li", class_="next")
    while next_page:
        next_page_url = next_page.find("a")["href"]
        next_page_url = category_url.replace("index.html", next_page_url)
        page = requests.get(next_page_url)
        soup = BeautifulSoup(page.content, "html.parser")
        books = soup.find_all("h3")
        for book in books:
            books_urls.append(
                "http://books.toscrape.com/catalogue/"
                + book.find("a")["href"].replace("../", "")
            )
        next_page = soup.find("li", class_="next")

    return books_urls


# URL de la page principale
url = "http://books.toscrape.com/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Recherche des URLs des catégories
categories = soup.find("ul", class_="nav nav-list").find_all("li")
categories_urls = [
    "http://books.toscrape.com/" + category.find("a")["href"] for category in categories
]

# Création du dossier principal
if not os.path.exists("Books"):
    os.makedirs("Books")

# Parcours de chaque catégorie
for category_url in categories_urls:
    page_url = category_url
    soup = BeautifulSoup(requests.get(page_url).content, "html.parser")
    category_name = soup.find("li", class_="active").text.strip()
    print(f"Scraping {category_name} category...")

    # Création d'un dossier pour la catégorie
    category_folder = os.path.join("Books", category_name)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    # Ouverture du fichier CSV pour écrire les informations des livres
    with open(
        os.path.join(category_folder, "books.csv"),
        "w",
        encoding="utf-8-sig",
        newline="",
    ) as csvfile:
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
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Écriture des informations de chaque livre dans le fichier CSV
        for book_url in get_books_urls(page_url):
            book_info = get_book_info(book_url)
            writer.writerow(book_info)

print("Scraping completed!")
