# --- Create a playlist in Spotify for the specified moment in time. ---

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.environ.get("Client_ID"),
    client_secret=os.environ.get("Client_TOKEN"),
    redirect_uri="http://example.com",
    show_dialog=True,
    cache_path="token.txt",
    username=os.environ.get("U_NAME"),
    scope="playlist-modify-private",
))
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(URL)
songs_web = BeautifulSoup(response.text, "html.parser")

top_songs = songs_web.select("li ul li h3")

top_songs_list = [n.getText().strip() for n in top_songs]

result = [sp.search(title)["tracks"]["items"][0]["uri"] for title in top_songs_list]

playlist_id = sp.user_playlist_create(user=user_id, public=False, name=f"{date} BillBoard-100")['id']

sp.playlist_add_items(playlist_id=playlist_id, items=result)
