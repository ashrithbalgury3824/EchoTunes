# spotify_recommender.py

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

# Set your Spotify Client ID and Secret
os.environ['SPOTIPY_CLIENT_ID'] = '311f0d83fa8e4176abcaa3aa1199e6e5'
os.environ['SPOTIPY_CLIENT_SECRET'] = '02c122fb6ea84a22932939f5ce52bd94'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

def recommend_songs(mood, genre, activity, time_of_day, language):
    # Define search query based on inputs
    query = f"{mood} {genre} {activity} {time_of_day} {language}"
    
    # Search Spotify for tracks based on the query
    results = sp.search(q=query, type='track', limit=5)
    
    # Parse the results
    songs = []
    for item in results['tracks']['items']:
        song = {
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'url': item['external_urls']['spotify']
        }
        songs.append(song)

    return songs
