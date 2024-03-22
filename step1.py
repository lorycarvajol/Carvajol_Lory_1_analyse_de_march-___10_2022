# Importation des modules nécessaires
import requests
from bs4 import BeautifulSoup
import csv

# URL de la page à scraper
url = "http://books.toscrape.com/index.html"

# Envoi d'une requête HTTP à l'URL spécifiée et analyse du contenu HTML avec BeautifulSoup
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


# Définition de la fonction pour extraire les informations d'une page de livre spécifique
def scrape_book_page(url):
    # Envoi d'une requête HTTP à l'URL spécifiée et analyse du contenu HTML avec BeautifulSoup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Extraction des informations spécifiques de la page de livre
    title = soup.find("h1").text
    price = soup.find("p", class_="price_color").text
    stock = soup.find("p", class_="instock availability").text.strip()

    # Extraction de la description (avec vérification si l'élément existe)
    description_element = soup.find("div", id="product_description")
    description = (
        description_element.next_sibling.next_sibling.text.strip()
        if description_element
        else ""
    )

    category = soup.find("ul", class_="breadcrumb").find_all("a")[2].text
    rating = soup.find("p", class_="star-rating")["class"][1]
    image_url = soup.find("div", class_="item active").find("img")["src"]
    table = soup.find("table", class_="table table-striped")
    rows = table.find_all("tr")
    upc = rows[0].find("td").text
    product_type = rows[1].find("td").text
    price_excluding_tax = rows[2].find("td").text
    price_including_tax = rows[3].find("td").text
    tax = rows[4].find("td").text
    availability = rows[5].find("td").text

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
        "image_url": image_url,
    }


# URL d'une page de livre spécifique à scraper
url = "http://books.toscrape.com/catalogue/the-picture-of-dorian-gray_270/index.html"

# Appel de la fonction scrape_book_page avec l'URL spécifique pour extraire les informations
scraped_data = scrape_book_page(url)

# Écriture des données extraites dans un fichier CSV lisible et clair
with open("books.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=scraped_data.keys())

    # Écriture de l'en-tête du fichier CSV
    writer.writeheader()

    # Écriture des données dans le fichier CSV
    writer.writerow(scraped_data)
