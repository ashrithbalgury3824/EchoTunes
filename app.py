from flask import Flask, request, jsonify, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Initialize Spotify client credentials
client_id = "311f0d83fa8e4176abcaa3aa1199e6e5"
client_secret = "02c122fb6ea84a22932939f5ce52bd94"

auth_manager = SpotifyClientCredentials(client_id='311f0d83fa8e4176abcaa3aa1199e6e5', client_secret='02c122fb6ea84a22932939f5ce52bd94')
sp = spotipy.Spotify(auth_manager=auth_manager)

def fetch_songs_for_preferences(mood, genre, language, offset=0):
    # Keywords for independent and movie music
    independent_keywords = ["indie", "independent", "unsigned", "alternative"]
    bollywood_keywords = ["Bollywood", "Hindi film", "movie", "soundtrack"]

    # Building query for tracks
    query = f"{mood} {genre} " + " ".join(independent_keywords + bollywood_keywords)

    # Adding language to the query
    if language.lower() == "english":
        # Construct the query without specifying "english" as Spotify defaults to English songs
        query = f"{mood} {genre} " + " ".join(independent_keywords + bollywood_keywords)
    else:
        # Include the language keyword if it's not English
        query = f"{mood} {genre} " + " ".join(independent_keywords + bollywood_keywords) + f" {language.lower()}"

    # Fetch recommendations

    # Fetch recommendations
    results = sp.search(q=query, type='track', limit=10, offset=offset)
    songs = []

    for item in results['tracks']['items']:
        # Filtering criteria
        if ('children' not in item['name'].lower() and 
            'kids' not in item['name'].lower() and 
            item['duration_ms'] > 120000):  # Exclude short tracks
            song = {
                'id': item['id'],
                'name': item['name'],
                'artist': item['artists'][0]['name'],
                'link': item['external_urls']['spotify'],
                'album_cover': item['album']['images'][0]['url']
            }
            songs.append(song)

    # If no songs found, use Spotify recommendations API as a fallback
    if not songs:
        try:
            recommendations = sp.recommendations(seed_genres=[genre], limit=10)
            for track in recommendations['tracks']:
                song = {
                    'id': track['id'],
                    'name': track['name'],
                    'artist': track['artists'][0]['name'],
                    'link': track['external_urls']['spotify'],
                    'album_cover': track['album']['images'][0]['url']
                }
                songs.append(song)
        except Exception as e:
            print(f"Error fetching recommendations: {e}")

    return songs

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    mood = data['mood']
    genre = data['genre']
    language = data['language']
    offset = data.get('offset', 0)

    recommendations = fetch_songs_for_preferences(mood, genre, language, offset)
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
