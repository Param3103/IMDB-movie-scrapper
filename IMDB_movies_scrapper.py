# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:39:11 2020

@author: -
"""

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=F22A2RC934X0Q4NDWHBA&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_7'
my_url2 = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

#opening connection graabbing page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

uClient2 = uReq(my_url2)
page2_html = uClient2.read()
uClient2.close()
#html parsing
page_soup = soup(page_html, "html.parser")
movies = []

containers = page_soup.findAll("td", {"class":"titleColumn"})
ratings = page_soup.findAll("td", {"class": "ratingColumn imdbRating"})
for i in containers:
    movie = [i.text, ratings[containers.index(i)].text]
    movies.append(movie)
    # print(i.text)
   #  print('Rating:' + ratings[containers.index(i)].text)

page2_soup = soup(page2_html, "html.parser")

containers = page2_soup.findAll("td", {"class":"titleColumn"})
ratings = page2_soup.findAll("td", {"class": "ratingColumn imdbRating"})
for i in containers:
    movie = [i.text, ratings[containers.index(i)].text]
    movies.append(movie)

def sorts(sorting):
    return(sorting[1])

movies.sort(key=sorts)
