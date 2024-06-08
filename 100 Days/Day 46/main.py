import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

client_id = "360b17b01c5f408987d9d3911aec1d42"
client_secret = "231f2ee09ba54d36a44397360a9ab6ea"

year = input("Which year do you want to travel to? Please provide the year in this format YYYY: ")
month = input("Please provide the month in this format MM: ")
day = input("DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}"

response = requests.get(url=URL)
contents = response.text
soup = BeautifulSoup(contents, "html.parser")

title = soup.select("li ul li h3")
title_list = [items.getText().strip() for items in title]
print(title_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt",
        username="Jianxun"
    )
)

user_id = sp.current_user()["id"]

song_uri = []
for song in title_list:
    results = sp.search(q=f"track:{song} year:{year}", type="track")
    print (results)
    try:
        uri = results["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name="top 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)
