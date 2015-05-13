import json

import requests

from cans.settings import MUSICBRAINZ


class MusicBrainz(object):

    URL = MUSICBRAINZ['URL']
    PARAMS = MUSICBRAINZ['PARAMS']
    SEARCH_TYPES = [
        'artist',
        'release',
        'release-group',
        'recording',
        'work',
        'label',
    ]

    def search(self, query, search_type):

        if search_type not in self.SEARCH_TYPES:
            raise NotImplementedError('Search type not supported')

        url = self.URL + search_type + '?query=' + query + self.unpack_params(self.PARAMS)
        r = requests.get(url, headers=MUSICBRAINZ['HEADERS'])

        return json.loads(r.text)

    def get_artist(self, mb_id):
        url = self.URL + 'artist/' + mb_id + '?' + self.unpack_params(self.PARAMS)
        r = requests.get(url, headers=MUSICBRAINZ['HEADERS'])

        return json.loads(r.text)

    def get_artist_image(self):
        pass

    @staticmethod
    def unpack_params(params):
        unpacked = ''
        for key in params:
            unpacked += '&' + key + '=' + params[key]
        return unpacked
