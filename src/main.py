from extract_data import extract_data
from manage_data import write_to_csv

english_movie_url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
hindi_movie_url = "https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=F22A2RC934X0Q4NDWHBA&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_7"

def main():
    movies = extract_data(hindi_movie_url) + extract_data(english_movie_url)
    movies.sort(key=lambda movie: movie.released_year)
    write_to_csv(movies, 'IMDBmovies.csv')


if __name__ == "__main__":
    main()
