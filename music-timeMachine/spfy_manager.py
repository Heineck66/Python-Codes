import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from song_class import Song
import os
from pprint import pprint

# spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = "http://localhost/"


class SpotifyManager:
    def __init__(self) -> None:
        self.spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="http://localhost/",
                client_id=SPOTIPY_CLIENT_ID,
                client_secret=SPOTIPY_CLIENT_SECRET,
                show_dialog=True,
            )
        )
        self.user_id = self.spotify.current_user()["id"]

        print(self.user_id)

    def search_songs_id(self, songs=list[Song]):
        songs_uris = []
        for song in songs:
            result = self.spotify.search(q=f"track:{song.name} artist:{song.artist}", limit=1, type="track")
            items = result["tracks"]["items"]

            # for item in items:
            #     for artist in item["artists"]:
            #         pprint(f'{item["name"]} - {artist["name"]}')

            try:
                uri = items[0]["uri"]
                songs_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
        print(songs_uris)
        return songs_uris

    def create_playlist(self, date, song_uris, public=False):
        playlist = self.spotify.user_playlist_create(user=self.user_id, name=f"{date} Billboard 100", public=public)
        print("List created!")
        self.add_song_playlist(playlist, song_uris)

    def track_info(self, track_id):
        track = self.spotify.track(track_id)
        return track

    def add_song_playlist(self, playlist, song_uris):
        self.spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
