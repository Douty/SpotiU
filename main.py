import spotipy
import os 
from dotenv import load_dotenv 
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()
Spotipy_client_id = os.getenv("SPOTIFY_CLIENT_ID")
Spotipy_client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
Spotipy_Redirect_url = os.getenv("SPOTIPY_REDIRECT_URI")

scope = "user-top-read","user-follow-read",

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def user_top_artists(limit,offset,time_range):
    results_artists = sp.current_user_top_artists(limit=limit,offset=offset,time_range=time_range)
    
    for idx,  artists in enumerate(results_artists["items"]):
        return idx, artists["name"], artists


#Fix: WHen there is two artists within the same song, the song prints twice showcasing the same song.
def user_top_tracks(limit,offset,time_range):
    results_tracks = sp.current_user_top_tracks(limit=limit,offset=offset,time_range=time_range)
    
    for idx, tracks in enumerate(results_tracks["items"]):
        album = tracks["album"]
        for artist in tracks["artists"]:
            return(idx,"Album: " + album["name"],",", "Song: " + tracks["name"],  ", " + "Artist: " + artist["name"])
        
            
