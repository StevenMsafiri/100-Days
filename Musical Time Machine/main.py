import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "5a9baddb6c4049e0b740961a8269c716"
CLIENT_SECRET = "2b68164a9c24438891b69e18e4220a1f"

access_token = "BQC7DKdX8qMvafQn2XPz3xGdK_WILgAVvf_WeljsCEE5tii5QswBe0BCMaqYUo-LhqkqG3X1-G3FAEMK6G6EgJrihHsefnh5hJoFG5u8nexEK8VJuIlTyOlFgn4rQ7ojIPDN7KKQjfQ7vTNSYfsEj7XkHgbD_6B4Iuc7kBrnyAKXLQ3PMFp1nrPGRNaGZBdVcn7alGfWWPC8khO1XGXfvkwvqr5d_UKWHA6fdHXsvKq1T5s10f9KaGTpvkqqFV8swmzbhQ9EeIAcZkxguCnk7w"

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
# print(user_id)

endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"

headers = {
    "Authorization":f"Bearer {access_token}",
    "Content-Type": "application/json"
}

body = {
    "name": f"Billboard Classic Throw-Back upto {date}",
    "description": "My first playlist of billboard top 100",
    "public": False,
}

# Creates a playlist
# spotify_response = requests.post(url=endpoint, headers=headers, json= body)

# Creating a second playlist for another date
second_playlist_body = {
    "name": f"{date} Billboard Top 1000",
    "description": f"Hot songs from billboard upto {date}",
    "public": False,
}

# create_response = requests.post(url=endpoint, headers=headers, json=second_playlist_body)
# print(create_response.text)

# Getting the data of the created playlist
spotify_response = requests.get(url=endpoint, headers=headers)
playlist_data = spotify_response.json()
# print(playlist_data)

playlist_id = playlist_data["items"][0]["id"]
# print(playlist_id)

adding_url =f"{endpoint}/{playlist_id}/tracks"
# print(adding_url)

# List of songs by the spotify uri
track_uris = []

for song in all_songs:
    # Searching the song on spotify
    result =sp.search(q=song, type="track", limit=1)
    try:
        track_uri = result['tracks']['items'][0]['uri']  # Get the track URI
        track_uris.append(track_uri)
    except IndexError:
        print(f"Song '{song}' not found on Spotify, skipping.")

print(track_uris)

if track_uris:
    add_tracks_endpoint = adding_url
    add_tracks_headers = headers
    add_tracks_body = {
        "uris": track_uris
    }

    add_tracks_response = requests.post(url=add_tracks_endpoint, headers =add_tracks_headers, json=add_tracks_body)
    print(add_tracks_response.text)
    print(add_tracks_response.json())


""""The best solution"""
# user_id = sp.current_user()["id"]
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]
#
# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# # print(playlist)
#
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)



