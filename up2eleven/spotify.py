import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import up2eleven

class Spotify(spotipy.Spotify):
    def get_artist_id(self, artist, return_closest_artist=True, limit=10) :
        query_return = self.search(artist, limit=limit, type='artist')['artists']['items']
        if return_closest_artist:
            artist_id = query_return[0]['id']
        else:
            choices_list = []
            for i in range(len(query_return)):
                choices_list.append(query_return[i]['name'])
            print(f'We found the following artists on Spotify matching "{artist}":')
            for i, choice in enumerate(choices_list):
                print(f"{i}  {choices_list[i]}")
            print(f"Please type the number corresponding to the artist you're interested in.")
            selection = int(input())
            if selection not in range(len(query_return)):
                print(f"Input not in range")
                return
            artist_id = query_return[selection]['id']
        return artist_id

class SpotifyClientCredentials(spotipy.oauth2.SpotifyClientCredentials):
    pass

