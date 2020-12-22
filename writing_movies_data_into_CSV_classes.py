import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import csv

my_url = 'https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=F22A2RC934X0Q4NDWHBA&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_7'
my_url2 = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

class ExtractData:
    def open_page(self):
        uClient = uReq(self)
        page_html = uClient.read()
        uClient.close()
        return(page_html)
    def extract_data(page_html):
        movies = []
        page_soup = soup(page_html, "html.parser")
        containers = page_soup.findAll("td", {"class": "titleColumn"})
        ratings = page_soup.findAll("td", {"class": "ratingColumn imdbRating"})
        for i in containers:
            movie = [i.text, ratings[containers.index(i)].text]
            movies.append(movie)
        return(movies)
class ManageData:
    def clean_data(movies):
        for movie in movies:
            for i in movie:
                movie[movie.index(i)] = re.sub('\n', '', i)
            movie[0] = movie[0][14:-1] + ')'
        return(movies)
    def write_to_csv(movies, filename):
        with open(filename, 'w') as file:
            csv_writer = csv.writer(file)
            for line in movies:
                if len(line) != 0:
                    csv_writer.writerow(line)
    def sorts(sorting):
        return(sorting[1])
movies = []
website1 = ExtractData.open_page(my_url)
website2 = ExtractData.open_page(my_url2)
for i in ExtractData.extract_data(website1):
    movies.append(i)
for i in ExtractData.extract_data(website2):
    movies.append(i)
movies.sort(key=ManageData.sorts)
movies = ManageData.clean_data(movies)
ManageData.write_to_csv(movies, 'IMDBmovies.txt')
print('done')
