import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import numpy as np
import pandas as pd

# User input for Spotify API credentials
client_id = "311f0d83fa8e4176abcaa3aa1199e6e5"
client_secret = "02c122fb6ea84a22932939f5ce52bd94"

auth_manager = SpotifyClientCredentials(client_id="311f0d83fa8e4176abcaa3aa1199e6e5", client_secret="02c122fb6ea84a22932939f5ce52bd94")
sp = spotipy.Spotify(auth_manager=auth_manager)

# Get artist names from the user
name = input("Enter the names of artists separated by commas: ").split(',')

# Search for each artist and fetch the first result
for artist in name:
    print(f"Searching for artist: {artist.strip()}")
    result = sp.search(artist.strip()) 
    if result['tracks']['items']:
        print(f"Found {result['tracks']['items'][0]['artists'][0]['name']}")
        artists_uris = result['tracks']['items'][0]['artists'][0]['uri']
        artist_albums = sp.artist_albums(artists_uris, album_type='album')
        
        # Store artist's albums' names and URIs
        artist_album_names = []
        artist_album_uris = []
        for album in artist_albums['items']:
            artist_album_names.append(album['name'])
            artist_album_uris.append(album['uri'])
        
        # Display albums found
        print(f"Albums found for {artist.strip()}: {artist_album_names}")

        # Function to get songs from an album
        def album_songs(uri, album_name):
            spotify_albums[uri] = {
                'album': [],
                'track_number': [],
                'id': [],
                'name': [],
                'uri': []
            }
            tracks = sp.album_tracks(uri)
            for track in tracks['items']:
                spotify_albums[uri]['album'].append(album_name)
                spotify_albums[uri]['track_number'].append(track['track_number'])
                spotify_albums[uri]['id'].append(track['id'])
                spotify_albums[uri]['name'].append(track['name'])
                spotify_albums[uri]['uri'].append(track['uri'])
        
        spotify_albums = {}
        for uri, name in zip(artist_album_uris, artist_album_names):
            album_songs(uri, name)
            print(f"Songs for album '{name}' have been added.")
        
        # Function to get audio features for each song
        def audio_features(album):
            spotify_albums[album].update({
                'acousticness': [],
                'danceability': [],
                'energy': [],
                'instrumentalness': [],
                'liveness': [],
                'loudness': [],
                'speechiness': [],
                'tempo': [],
                'valence': [],
                'popularity': []
            })
            for track in spotify_albums[album]['uri']:
                features = sp.audio_features(track)[0]
                if features:
                    spotify_albums[album]['acousticness'].append(features['acousticness'])
                    spotify_albums[album]['danceability'].append(features['danceability'])
                    spotify_albums[album]['energy'].append(features['energy'])
                    spotify_albums[album]['instrumentalness'].append(features['instrumentalness'])
                    spotify_albums[album]['liveness'].append(features['liveness'])
                    spotify_albums[album]['loudness'].append(features['loudness'])
                    spotify_albums[album]['speechiness'].append(features['speechiness'])
                    spotify_albums[album]['tempo'].append(features['tempo'])
                    spotify_albums[album]['valence'].append(features['valence'])
                    spotify_albums[album]['popularity'].append(sp.track(track)['popularity'])

        for album in spotify_albums:
            audio_features(album)
            print(f"Audio features for album '{spotify_albums[album]['album'][0]}' have been added.")

    else:
        print(f"No results found for {artist.strip()}")

# Compile all data into a DataFrame
dic_df = {key: [] for key in ['album', 'track_number', 'id', 'name', 'uri', 
                              'acousticness', 'danceability', 'energy', 
                              'instrumentalness', 'liveness', 'loudness', 
                              'speechiness', 'tempo', 'valence', 'popularity']}

for album in spotify_albums:
    for feature in spotify_albums[album]:
        dic_df[feature].extend(spotify_albums[album][feature])

dataframe = pd.DataFrame.from_dict(dic_df)

# Filter the DataFrame based on user input
min_popularity = int(input("Enter minimum popularity score (0-100) for filtering: "))
final_df = dataframe[dataframe['popularity'] >= min_popularity].sort_values('popularity', ascending=False).drop_duplicates('name')

# Output DataFrame as CSV
save_to_csv = input("Would you like to save the data to a CSV file? (yes/no): ").strip().lower()
if save_to_csv == 'yes':
    filename = input("Enter the CSV file name (without extension): ")
    final_df.to_csv(f"{filename}.csv", index=False)
    print(f"Data saved to {filename}.csv")
else:
    print("Data not saved.")

# Display the top songs based on popularity
print("\nTop songs based on popularity:\n")
print(final_df[['name', 'popularity']].head())
