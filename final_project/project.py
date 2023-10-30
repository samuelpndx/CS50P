from spotipy.oauth2 import SpotifyClientCredentials
from ytmusicapi import YTMusic
import spotipy


def main():
    client_id, client_secret = set_up_spotify()
    auth_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret,
    )

    global sp
    sp = spotipy.Spotify(auth_manager=auth_manager)

    global ytmusic
    ytmusic = YTMusic("oauth.json")

    username = get_username()
    list_of_playlists = sp.user_playlists(username)
    dict_play = playlists_to_dict(list_of_playlists)

    print(create_youtube_playlists(dict_play))


def get_user_input(message=""):
    return input(message)


def set_up_spotify():
    client_id = get_user_input("Client ID: ").strip()
    client_secret = get_user_input("Client secret: ").strip()
    return (client_id, client_secret)


def get_username():
    username = get_user_input("Username: ").strip()
    return username


def playlists_to_dict(list_of_playlists):
    result = {}
    for playlist in list_of_playlists["items"]:
        tracks = get_tracks(playlist["id"])
        result[playlist["name"]] = tracks

    for key in result.keys():
        print(f"🔍🎼 {key}")
        mapped = map(get_video_id, result[key])
        result[key] = list(mapped)

    return result


def get_tracks(playlist_id):
    list_of_tracks = []
    tracks = sp.playlist_tracks(playlist_id)
    for track in tracks["items"]:
        if track["track"] != None:
            list_of_tracks.append(
                f"{track['track']['name']} - {track['track']['artists'][0]['name']}"
            )
    return list_of_tracks


def get_video_id(track):
    search_result = ytmusic.search(track, filter="songs", limit=1)[0]["videoId"]
    if search_result:
        print(f"✔️ {track}")
    else:
        print(f"❌ {track}")
    return search_result


def create_youtube_playlists(dict_play):
    for key in dict_play.keys():
        ytmusic.create_playlist(title=key, description="", video_ids=dict_play[key])
    return "Success"


if __name__ == "__main__":
    main()
