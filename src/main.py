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
        print(movies)
        ManageData.write_to_csv(movies, 'IMDBmovies.csv')

Main.process