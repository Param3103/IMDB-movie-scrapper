import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re as regex
import csv

hindi_movie_url = 'https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=F22A2RC934X0Q4NDWHBA&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_7'
english_movie_url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

class Movie:
    def __init__(self, released_year, name, rating):
        self.released_year = released_year
        self.name = name
        self.rating = rating

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

class ManageData:
    # remove \n tags in html code that indicates to print in next line but we do not need them
    def remove_line_break(movies):
        for movie in movies:
            movie.released_year = regex.sub('\n', '', movie.released_year)
            movie.name = regex.sub('\n', '', movie.name)
            movie.rating = regex.sub('\n', '', movie.rating)
            movie.name = movie.name[13:-1]
        return(movies)
    def remove_start_space(movies):
        for movie in movies:
            if movie[0][0] == ' ':
                movie[0].remove(movie[0][0])
            else:
                continue

    def write_to_csv(movies, filename):
        with open(filename, 'w') as file:
            csv_writer = csv.writer(file)
            for movie in movies:
                csv_writer.writerow(str(movie.released_year))
                csv_writer.writerow(str(movie.name))
                csv_writer.writerow(str(movie.rating))

    def sorts(sorting):
        return(sorting.rating)
movies = []
website1 = ExtractData.open_page(hindi_movie_url)
website2 = ExtractData.open_page(english_movie_url)
for i in ExtractData.extract_data(website1):
    movies.append(i)
for i in ExtractData.extract_data(website2):
    movies.append(i)
movies.sort(key=ManageData.sorts)
movies = ManageData.remove_line_break(movies)
for movie in movies:
    print(movie.name)
    print(movie.released_year)
    print(movie.rating)
ManageData.write_to_csv(movies, 'IMDBmovies.csv')