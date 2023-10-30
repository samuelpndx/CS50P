# Spotify to YouTube Music Playlist Importer
#### Video Demo:  https://vimeo.com/871465115
#### Description:
Introducing my Python program designed for seamless playlist migration from a Spotify user account to YouTube Music. This project allows users to transfer their curated playlists effortlessly. By providing Spotify client ID, client secret, and the source username, the program streamlines the process, ensuring a smooth transition of playlists to YouTube Music. Say goodbye to manual recreation and enjoy your favorite tunes on a new platform with ease. Try it now and elevate your music streaming experience!

#### Requirements
Before using this script, ensure that you have Python installed on your system. You can install the required packages using the following commands:


```bash
pip install spotipy
pip install ytmusicapi
```

#### Usage

1. Generate a new app at https://developer.spotify.com/dashboard

2. Run this command to generate 'oauth.json' for authentication on YouTube Music.

```bash
ytmusicapi oauth
```
3. Execute the script using the following command:
```bash
python project.py

```
4. Input Credentials:
When prompted, enter your Spotify Client ID, Client Secret, and the Spotify username associated with the playlists you want to migrate.
5. Sit Back and Enjoy:
The script will authenticate with Spotify, fetch your playlists, map the tracks to YouTube Music, and create new playlists on YouTube Music.

#### Script Workflow
1. The script prompts for Spotify API credentials and the source username.
2. It retrieves the list of playlists from the provided Spotify username.
3. For each playlist, it fetches the tracks and maps them to YouTube Music.
4. The script creates new playlists on YouTube Music with the mapped tracks.

#### Notes
The script outputs the results of each track mapping, indicating success or failure.
Please note that YouTube Music's API limitations may impact the availability of certain tracks.
Feel free to reach out if you have any questions or encounter issues. Happy playlist migration!