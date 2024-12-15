from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
load_dotenv()
# Replace with your YouTube Data API key
# TODO CHANGE API
API_KEY = os.getenv('YOUTUBE_API_KEY')

def search_youtube(song_title, artist):
    # Build the YouTube API client
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    # Search query combining song title and artist
    query = f"{song_title} {artist}"
    
    # Execute the search
    request = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=1,
        type='video'
    )
    response = request.execute()
    
    # Extract the video link
    if 'items' in response and len(response['items']) > 0:
        video_id = response['items'][0]['id']['videoId']
        video_title = response['items'][0]['snippet']['title']
        video_link = f"https://www.youtube.com/watch?v={video_id}"
        # print(f"Title: {video_title}")
        # print(f"Link: {video_link}")
        return video_link
    else:
        print("No results found.")

def RUN_YOUTUBE():
    # Get user input for song title and artist
    song_title = input("Enter the song title: ")
    artist = input("Enter the artist: ")
    search_youtube(song_title, artist)

if __name__ == "__main__":
    RUN_YOUTUBE()
