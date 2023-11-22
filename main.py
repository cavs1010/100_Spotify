from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import requests
import re


auth_manager = SpotifyOAuth(client_id=os.environ['SPOTIPY_CLIENT_ID'],
                            client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
                            redirect_uri="http://google.com/",
                            scope=["playlist-modify-public", "user-library-read","user-modify-playback-state"])
sp = spotipy.Spotify(auth_manager=auth_manager)
sp_user_id = sp.current_user()['id']


target_date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD:")
if not re.match("\d{4}-\d{2}-\d{2}", target_date):
    raise ValueError("The date you included do not comply with the format expected")

year_date = int(target_date.split("-")[0])
range_year = 5
year_query = f"{year_date-5}-{year_date+5}"

response = requests.get(f"https://www.billboard.com/charts/hot-100/{target_date}")
if response.status_code != 200:
    raise Exception("Failed to retrieve data from the website")

soup = BeautifulSoup(response.text, 'html.parser')
song_info_list = soup.findAll(name="div", class_="o-chart-results-list-row-container")
song_names = [song_info.find(name="li", class_="lrv-u-width-100p").find(name="h3").get_text(strip=True) for song_info in song_info_list]
artist_names = [song_info.find(name="li", class_="lrv-u-width-100p").find(name="span").get_text(strip=True) for song_info in song_info_list]


if len(song_names) != len(artist_names):
    raise ValueError("Mismatch in lengths: The number of songs and artists does not match.")

list_track_ids = []

for index, song in enumerate(song_names):
    track_name = song.replace("'", "")
    artist_name = artist_names[index]
    query = f"artist:{artist_name} track:{track_name} year:{year_query}"
    results = sp.search(q=query, type="track", limit=3)
    try:
        track_id = results['tracks']['items'][0]["id"]
        list_track_ids.append(track_id)
    except Exception as a:
        print(f"The song {track_name} from {artist_name} could not be found.")
        continue

percentage_missing_songs = ((len(song_names)-len(list_track_ids))/len(list_track_ids))*100
print(f"The percentage of missing songs were {percentage_missing_songs:.1f}%.")


playlist = sp.user_playlist_create(user=sp_user_id, name=f"TM: {target_date}")
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=list_track_ids)

