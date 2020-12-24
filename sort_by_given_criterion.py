import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re as regex
import csv
from src.movie import Movie
from src.main import main
from src.extractdata import ExtractData
hindi_movie_url = 'https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=F22A2RC934X0Q4NDWHBA&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_7'
english_movie_url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

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
            movie.name = movie.name.strip()
        return(movies)

    def write_to_csv(movies, filename):
        with open(filename, 'w') as file:
            csv_writer = csv.writer(file)
            for movie in movies:
                csv_writer.writerow([movie.name, movie.released_year, movie.rating])

    def sorts(movie):
        return(movie.rating) # can sort by rating/name/year, just change here
movies = []
website1 = ExtractData.open_page(hindi_movie_url)
website2 = ExtractData.open_page(english_movie_url)
for i in ExtractData.extract_data(website1):
    movies.append(i)
for i in ExtractData.extract_data(website2):
    movies.append(i)
movies.sort(key=ManageData.sorts)
movies = ManageData.remove_line_break(movies)
movies = ManageData.remove_start_space(movies)
print(movies)
ManageData.write_to_csv(movies, 'IMDBmovies.csv')