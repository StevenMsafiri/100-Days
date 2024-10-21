import requests
from bs4 import BeautifulSoup

date = input("Which year would you like to travel to? Type the date in this format YYYY-MM-DD: ")

song_titles_endpoint = f"https://www.billboard.com/charts/hot-100/{date}"
# print(song_titles_endpoint)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = requests.get(url=song_titles_endpoint, headers=headers)
billboard_page = response.text
# print(billboard_page)

soup = BeautifulSoup(billboard_page, "html.parser")
# print(soup.prettify())

top_hundred = soup.select("li > h3.c-title")
# print(top_hundred)

all_songs = [song.getText().strip() for song in top_hundred]
print(all_songs)