import requests
from bs4 import BeautifulSoup
import os


url = "http://books.toscrape.com/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


def get_book_images_urls():
    book_images_urls = []
    for page_number in range(1, 51):
        page_url = (
            "http://books.toscrape.com/catalogue/page-" + str(page_number) + ".html"
        )
        page = requests.get(page_url)
        soup = BeautifulSoup(page.content, "html.parser")
        book_images = soup.find_all("img")
        for book_image in book_images:
            book_images_urls.append(book_image["src"])
    return book_images_urls


def download_book_images():
    book_images_urls = get_book_images_urls()
    if not os.path.exists("images"):
        os.makedirs("images")
    for book_image_url in book_images_urls:
        book_image = requests.get("http://books.toscrape.com/" + book_image_url)
        with open("images/" + book_image_url.split("/")[-1], "wb") as f:
            f.write(book_image.content)


download_book_images()
