import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "5a9baddb6c4049e0b740961a8269c716"
CLIENT_SECRET = "2b68164a9c24438891b69e18e4220a1f"

access_token = "BQBZ58ClIDwkRZwVBOOwjiM52PJKsr-cJ8PtwkzJCTd7M3KWm9BkIA9zyd8qU4EcYSvUDnXKRqlWW5pmK-6iWDR8FfDZ4xpWuvNl_axcoKp35FNRky_cCIymE43Qrh_AnIcUWZZgduzP-8EnmZEwXo1WjYD3qxJVQdWzjmGmSgTBLuWnPR23QhR6AIsch5oqbhqBZL_BiDITerVDU0SwMcNiJtULbDQ_pfAlNPhQH-U1uukE4WAXRhw1LEijW1GTiTTHgrNHLCc"

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

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= CLIENT_ID,
                                               client_secret= CLIENT_SECRET,
                                               redirect_uri="https://example.com",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               scope="playlist-modify-public playlist-modify-private"))


user_id = sp.current_user()["id"]
print(user_id)

endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"

headers = {
    "Authorization":f"Bearer {access_token}",
    "Content-Type": "application/json"
}

body = {
    "name": "Classic Throw-Back",
    "description": "My first playlist",
    "public": False,
}

# Creates a playlist
# spotify_response = requests.post(url=endpoint, headers=headers, json= body)

spotify_response = requests.get(url=endpoint, headers=headers)
playlist_data = spotify_response.json()
# print(playlist_data)

playlist_id = playlist_data["items"][0]["id"]

adding_url =f"{endpoint}/{playlist_id}/tracks"






