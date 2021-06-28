def write_to_csv(movies, filename):
    with open(filename, 'w+') as file:
        print("released_year,name,rating", file=file)
        for movie in movies: print(movie, file=file)
