import requests
from bs4 import BeautifulSoup
import re

def search_youtube(song_title, artist):
    # Format the search query
    query = f"{song_title} {artist}".replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    # print(f"https://www.youtube.com/results?search_query={query}")
    # Send a request to YouTube
    
    response = requests.get(url)
    pattern = r"\/watch\?v=([a-zA-Z0-9_-]+)"
    if response.status_code != 200:
        print("Failed to retrieve YouTube search results.")
        return

    video_ids = re.findall(pattern, response.text)

    video_links = [f"https://www.youtube.com/watch?v={video_ids[0]}" for video_id in video_ids]
    # print(video_links[0])
    return video_links[0]

    # Print the video links
    # for link in video_links:
    #     print(link)

    # Check if the request was successful
    
    
    # # Parse the response content
    # soup = BeautifulSoup(response.text, 'html.parser')
    # # print(soup.prettify())
    # # open("output.html", "w",encoding='utf-8').write(soup.prettify())
    # # Find the first video link
    # for link in soup.find_all('a', href=True):
    #     href = link['href']
    #     if "/watch?v=" in href:
    #         video_link = f"https://www.youtube.com{href}"
    #         print(f"First video link: {video_link}")
    #         return
    
    # print("No video links found.")

def main():
    # Get user input for song title and artist
    song_title = input("Enter the song title: ")
    artist = input("Enter the artist: ")
    search_youtube(song_title, artist)

if __name__ == "__main__":
    main()
