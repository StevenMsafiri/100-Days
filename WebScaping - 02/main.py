from re import findall

import requests
from bs4 import BeautifulSoup
from lxml.html.diff import htmldiff_tokens

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# print(soup.prettify())


movies_titles = soup.find_all(name="h3", class_="title")
movies_titles.reverse()
# print(movies_titles)

with open(file="movies.txt", mode="w") as file:
    for movie in movies_titles:
        file.write(f"{movie.getText()}\n")
