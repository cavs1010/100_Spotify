from bs4 import BeautifulSoup
import requests
import re

target_date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD:")
if not re.match("\d{4}-\d{2}-\d{2}", target_date):
    raise ValueError("The date you included do not comply with the format expected")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{target_date}")
if response.status_code != 200:
    raise Exception("Failed to retrieve data from the website")

soup = BeautifulSoup(response.text, 'html.parser')
song_info_list = soup.findAll(name="div", class_="o-chart-results-list-row-container")
song_names = [song_info.find(name="li", class_="lrv-u-width-100p").find(name="h3").get_text(strip=True) for song_info in song_info_list]
artist_names = [song_info.find(name="li", class_="lrv-u-width-100p").find(name="span").get_text(strip=True) for song_info in song_info_list]

print(song_names)
print(artist_names)
