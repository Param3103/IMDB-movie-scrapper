from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from movie import Movie

def extract_data(url):
    with urlopen(url) as uClient: page_html = uClient.read()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("td", {"class": "titleColumn"})
    ratings = page_soup.findAll("td", {"class": "ratingColumn imdbRating"})
    return [Movie.fromSoup(containers[i], ratings[i]) for i in range(min(len(containers), len(ratings)))]
