from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
from googleapiclient.discovery import build
from google.oauth2 import credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import time
from googleapiclient.errors import HttpError
import requests
import re

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
# Spotify API functions
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, data=data, headers=headers)
    json_result = json.loads(result.content)
    if "access_token" in json_result:
        return json_result["access_token"]
    else:
        raise ValueError("Failed to obtain access token from Spotify API")

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_songs_in_playlist(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    if result.status_code == 200:
        json_result = json.loads(result.content)["items"]
        return json_result
    else:
        raise ValueError("Failed to retrieve songs from Spotify playlist")

# YouTube API functions
def setup_youtube_client():
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_id_secret")
    scopes = ['https://www.googleapis.com/auth/youtube']

    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json',  # Path to your client secrets file
        scopes=scopes
    )

    credentials = flow.run_local_server(port=0)

    # Obtain an access token
    access_token = credentials.token

    # Set up the YouTube Data API client
    api_key = os.getenv("YOUTUBE_API_KEY")
    youtube = build('youtube', 'v3', credentials=credentials)

    return youtube

def search_video_id(title):
    query = title.replace(' ', '+')
    url = f"https://www.youtube.com/results?search_query={query}"

    response = requests.get(url)
    html_content = response.text

    video_ids = re.findall(r"\"videoId\":\"(\w{11})\"", html_content)
    if video_ids:
        return video_ids[0]  # Return the first video ID
    else:
        return None

def create_playlist(youtube):
    playlist_title = input("Enter playlist title:- ")
    playlist_description = 'Your Playlist Description'
    playlist_response = youtube.playlists().insert(
        part='snippet',
        body={
            'snippet': {
                'title': playlist_title,
                'description': playlist_description
            }
        }
    ).execute()

    if 'id' in playlist_response:
        playlist_id = playlist_response['id']
        print(f'Created playlist: {playlist_title} ({playlist_id})')
        return playlist_id
    else:
        raise ValueError("Failed to create a new playlist on YouTube")



def add_song_to_playlist(youtube, playlist_id, video_id):
    retry_count = 0
    while retry_count < 3:
        try:
            playlist_item_response = youtube.playlistItems().insert(
                part='snippet',
                body={
                    'snippet': {
                        'playlistId': playlist_id,
                        'position': 0,
                        'resourceId': {
                            'kind': 'youtube#video',
                            'videoId': video_id
                        }
                    }
                }
            ).execute()

            if 'id' in playlist_item_response:
                print("Added video to playlist")
                return
            else:
                raise ValueError("Failed to add the video to the playlist")
        except HttpError as e:
            if e.resp.status in [403, 500, 503, 409]:
                print(f"HttpError occurred while adding the video to the playlist: {str(e)}")
                retry_count += 1
                print(f"Retrying in 5 seconds ({retry_count}/3)")
                time.sleep(5)
            else:
                raise
        except Exception as e:
            print(f"An error occurred while adding the video to the playlist: {str(e)}")
            retry_count += 1
            print(f"Retrying in 5 seconds ({retry_count}/3)")
            time.sleep(5)

    print("Failed to add the video to the playlist after multiple attempts")



# Main code
def main():
    try:
        # Get Spotify token
        token = get_token()

        # Get playlist ID from user
        playlist_url = input("Enter playlist URL: ")
        playlist_id = playlist_url.removeprefix("https://open.spotify.com/playlist/")

        # Get songs from Spotify playlist
        songs = get_songs_in_playlist(token, playlist_id)

        # Set up YouTube API client
        youtube = setup_youtube_client()

        # Create a new playlist on YouTube
        playlist_id = create_playlist(youtube)

        # Search for songs on YouTube and add them to the playlist
        for idx, song in enumerate(songs):
            playlist_song = f"{song['track']['name']} by {song['track']['artists'][0]['name']}"
            video_id = search_video_id(playlist_song)
            add_song_to_playlist(youtube, playlist_id, video_id)

    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()