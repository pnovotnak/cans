from lastfm import LastFM
from musicbrainz import MusicBrainz
from .models import Artist, ReleaseGroup, Track


class API(object):

    def __init__(self):
        self.mb = MusicBrainz()
        self.lastfm = LastFM()

    def search(self, query, query_type):
        results = self.mb.search(query, query_type)[query_type+'s']
        objects = []

        for result in results:
            try:
                Artist.objects.get(mbid=result['id'])
            except Artist.DoesNotExist:

                artist_info = self.lastfm.get_artist_by_mbid(result['id'])

                if 'artist' in artist_info:
                    Artist(
                        name=artist_info['artist']['name'],
                        description=artist_info['artist']['bio']['content'],
                        mbid=result['id']
                    ).save()

        return objects
