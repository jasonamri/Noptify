import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
from dotenv import load_dotenv
load_dotenv()

scope = "user-modify-playback-state user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

sp.volume(90)


while 1:

    results = sp.current_user_playing_track()
    print(results)
    sleep(5)