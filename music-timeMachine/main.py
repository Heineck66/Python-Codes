from billboard_scraper import scrape_100_songs
from spfy_manager import SpotifyManager
from pprint import pprint
from song_class import Song

sp_mng = SpotifyManager()

# ------- Get user input ---------
# date_input = input("Give me a date (format YYYY-MM-DD): ")

# try:
#     year, month, day = map(int, date_input.split("-"))
# except ValueError:
#     print("Not valid format, please try again, YYYY-MM-DD (2020-08-12)")
#     exit()

# date_to_scrape = date_input
# --------- Scrape the songs from billboard
date_to_scrape = "2000-08-12"
songs = scrape_100_songs(date_to_scrape)


# ----- Search for ids and create list
ids_list = sp_mng.search_songs_id(songs)

sp_mng.create_playlist(2000, ids_list)


# pprint(li)
# print(track)
