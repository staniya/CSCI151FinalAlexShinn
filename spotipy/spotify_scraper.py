import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

artist_uri = {
    "lz_uri" : 'spotify:artist:36QJpDe2go2KgaRleHCDTp',
}

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(artist_uri["lz_uri"])

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()