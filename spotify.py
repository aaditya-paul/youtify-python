import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()
# Spotify API credentials and settings
# TODO CHANGE CREDS
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'playlist-read-private'

# Function to get playlist tracks
def get_playlist_tracks(playlist_id):
    # Authenticate using SpotifyOAuth
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE))
    
    # Retrieve tracks from the playlist
    results = sp.playlist_tracks(playlist_id)
    tracks = []

    # Loop through the items and collect track details
    while results:
        for item in results['items']:
            track = item['track']
            track_name = track['name']
            artist_name = ', '.join([artist['name'] for artist in track['artists']])
            tracks.append({'Track': track_name, 'Artist': artist_name})
        
        # Get next page of results if available
        results = sp.next(results)

    return tracks

# Main function
def RUN_SPOTIFY():
    # Replace with your Spotify playlist ID
    playlist_id = input("Enter the Spotify Playlist ID or URL: ").split('/')[-1].split('?')[0]
    
    print("Fetching playlist tracks...")
    tracks = get_playlist_tracks(playlist_id)

    # Save to CSV
    df = pd.DataFrame(tracks)
    df.to_csv(f'spotify_playlists\\spotify_playlist_tracks_{playlist_id}.csv', index=False)
    # print(f"Playlist tracks have been saved to 'spotify_playlist_tracks_{playlist_id}.csv'.")
    return f"spotify_playlist_tracks_{playlist_id}.csv"

# Run the main function
if __name__ == "__main__":
    RUN_SPOTIFY()
