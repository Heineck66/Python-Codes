import requests
from bs4 import BeautifulSoup
from song_class import Song
import re


def scrape_100_songs(date) -> list[Song]:
    url = f"https://www.billboard.com/charts/hot-100/{date}"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup.find_all("span", {"class": "chart-element__information"})

    top_songs = []
    for index, tag in enumerate(tags, start=1):
        song_name = tag.findChild("span", class_="chart-element__information__song").get_text()
        artist_text = tag.findChild("span", class_="chart-element__information__artist").get_text()
        artist = re.split("(&|Featuring)", artist_text)[0]
        song = Song(index, song_name, artist)
        top_songs.append(song)

    return top_songs
