import unittest
import csv
from main import movies
import re
data = []
with open('IMDBmovies.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for line in csv_reader:
        if len(line) != 0:
            data.append(line)
class Testing_Project(unittest.TestCase):
    #tests if all movies have been deposited into csv file
    def test_if_deposited(self):
        for movie in movies:
            for i in movie:
                movie[movie.index(i)] = re.sub('\n', '', i)
            movie[0] = movie[0][14:-1] + ')'
            self.assertIn(movie, data)
    # test if each movie value is a pair
    def test_is_pair(self):
        for movie in data[0: len(data)]:
            self.assertEqual(len(movie), 2)
    #tests if movies have been sorted according to rating
    def test_if_sorted_rating(self):
        for movie in data[0: len(data) - 1]:
            self.assertTrue(movie[1] <= data[data.index(movie) + 1][1])
    """
    def test_if_sorted_name(self):
            self.assertTrue(data == sorted(data[0])
    def test_if_sorted_released_year(self):
        for movie in data[0: len(data) - 1]:
            self.assertTrue(movie[1] <= data[data.index(movie) + 1][1])
    """
if __name__ == '__main__':
    unittest.main()
