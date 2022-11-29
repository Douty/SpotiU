import spotipy
import os 
import json
from dotenv import load_dotenv 
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()
Spotipy_client_id = os.getenv("SPOTIFY_CLIENT_ID")
Spotipy_client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
Spotipy_Redirect_url = os.getenv("SPOTIPY_REDIRECT_URI")

scope = "user-top-read","user-follow-read"
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

cat = sp.artist("0O1UtbTe4ca7HabaiMhYZ7")

#def user_top_genre(limit,offset,time_range):
    #results_genre = sp.current_user_top_artists(limit=limit,offset=offset,time_range=time_range)
    
    #for idx, genre in enumerate(results_genre["items"]):
        #for artist in tracks["artists"]:
            #return(idx,"Album: " + album["name"],",", "Song: " + tracks["name"],  ", " + "Artist: " + artist["name"])




#optimize 
def user_genre_sample_list():
    genres = []
    artists_short = sp.current_user_top_artists(limit=20,offset=0,time_range="short_term")
    artists_medium = sp.current_user_top_artists(limit=40,offset=0,time_range="medium_term")
    artists_long = sp.current_user_top_artists(limit=10,offset=0,time_range="long_term")
    for x in artists_short["items"]:
        genres.extend(x['genres'])
        for y in artists_medium['items']:
            genres.extend(y['genres'])
            for z in artists_long['items']:
                genres.extend(z['genres'])

    print(genres)

       

user_genre_sample_list()