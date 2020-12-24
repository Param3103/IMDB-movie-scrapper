import re as regex
import csv
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
ManageData