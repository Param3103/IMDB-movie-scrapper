from extract_data import ExtractData
from manage_data import ManageData
english_movie_url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
hindi_movie_url = "https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=F22A2RC934X0Q4NDWHBA&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_7"
class Main:
    def process(self):
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
        ManageData.write_to_csv(movies, 'IMDBmovies.csv')

Main.process(None)
