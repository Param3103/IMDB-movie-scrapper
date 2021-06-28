from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

class Movie:
    def __init__(self, released_year, name, rating):
        self.released_year = released_year.replace("\n", "")
        self.name = name.replace("\n", "")[13:-1].strip()
        self.rating = rating.replace("\n", "")

    def __str__(self):
        return ",".join([self.released_year, self.name, self.rating])

    @classmethod
    def fromSoup(cls, container, rating):
        return cls(container.text[-6: -2], container.text[2: -6], rating.text)


def extract_data(url):
    with urlopen(url) as uClient: page_html = uClient.read()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("td", {"class": "titleColumn"})
    ratings = page_soup.findAll("td", {"class": "ratingColumn imdbRating"})
    return [Movie.fromSoup(containers[i], ratings[i]) for i in range(min(len(containers), len(ratings)))]


def write_to_csv(movies, filename):
    with open(filename, 'w+') as file:
        print("released_year,name,rating", file=file)
        for movie in movies: print(movie, file=file)


english_movie_url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
hindi_movie_url = "https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=F22A2RC934X0Q4NDWHBA&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_7"

def main():
    movies = extract_data(hindi_movie_url) + extract_data(english_movie_url)
    movies.sort(key=lambda movie: movie.released_year)
    write_to_csv(movies, 'IMDBmovies.csv')


if __name__ == "__main__":
    main()
