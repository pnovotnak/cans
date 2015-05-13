import json

import requests

from cans.settings import LASTFM


class LastFM(object):

    URL = LASTFM['URL']
    PARAMS = LASTFM['PARAMS']
    SEARCH_TYPES = [
        'artist',
        'album',
        'tag',
        'track',
    ]

    """ Search is currently far too slow to be considered "usable"
    def search(self, query, search_type):

        if search_type not in self.SEARCH_TYPES:
            raise NotImplementedError('Search type not supported')

        params = self.PARAMS
        params['method'] = search_type + '.search'
        params[search_type] = query

        url = self.URL + "?" + self.pack_params(params)
        r = requests.get(url)

        return json.loads(r.text)
    """

    def get_artist_by_mbid(self, mbid):

        params = self.PARAMS
        params['method'] = 'artist.getinfo'
        params['mbid'] = mbid

        url = self.URL + '?' + self.pack_params(params)
        r = requests.get(url)

        return json.loads(r.text)

    def get_artist_image(self):
        pass

    @staticmethod
    def pack_params(params):
        unpacked = ''
        for key in params:
            unpacked += '&' + key + '=' + params[key]
        return unpacked
