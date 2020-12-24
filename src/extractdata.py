from urllib.request import urlopen
import bs4
from bs4 import BeautifulSoup as soup
from src.movie import Movie

class ExtractData:

    def open_page(url):
        uClient = urlopen(url)
        page_html = uClient.read()
        uClient.close()
        return(page_html)

    def extract_data(page_html):
        movies = []
        page_soup = soup(page_html, "html.parser")
        containers = page_soup.findAll("td", {"class": "titleColumn"})
        ratings = page_soup.findAll("td", {"class": "ratingColumn imdbRating"})
        for container in containers:
            name = container.text[2: -6]
            year = container.text[-6: -2]
            movie = Movie(year, name, ratings[containers.index(container)].text)
            movies.append(movie)
        return(movies)
ExtractData