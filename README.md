This is a simple Python program designed to solve a common and frustrating issue: converting Spotify playlists to YouTube. As an avid music lover who primarily uses YouTube, I needed a way to easily convert my friend's Spotify playlists.

To use this program, follow these steps:

Register on the Spotify Developer page and create an app to obtain the client ID and client secret.
Register on the YouTube Cloud Console, create a project, and enable the YouTube Data API 3.
Generate API keys and credentials (client ID and client secret) for YouTube API, ensuring the API key is restricted to YouTube Data API 3.
Register the app as a desktop app on the YouTube Cloud Console and publish it.
Download the credential JSON file and place it in the same folder as the code.
Create an `.env` file in the same folder and initialize all the credentials and API keys.
Install the required modules.
Run the program, and it should work smoothly. Enjoy! 🥳
During the development of this project, I encountered several challenges, including connecting to Spotify and extracting data from the Spotify API, organizing the extracted data for easy use, connecting to the YouTube API, and working around the daily quota limit of the YouTube API.

To overcome these challenges, I followed a helpful video tutorial for Spotify OAuth and access token retrieval. Since YouTube has a daily quota, I couldn't add a full playlist using the YouTube API alone. To address this, I used web scraping to search and retrieve video IDs, and then utilized the YouTube API to create playlists and add songs. The YouTube authentication process was facilitated with the help of ChatGPT.

One limitation of the program is that it currently only supports the first 100 songs of a playlist, due to a limitation in Spotify. To overcome this, you could implement offset functionality to retrieve more songs. As for the YouTube daily quota limitation, I'm still exploring potential solutions.

I hope you find this program useful, and I'm open to any suggestions or improvements. Thank you!
