from django.test import TestCase

from .musicbrainz.base import MusicBrainz
from .lastfm.base import LastFM

from .api import API


class APITestCase(TestCase):
    """ Test the overarching API class that ties together all of the disparate API
    """

    def setUp(self):
        self.api = API()

    def test_search(self):
        results = self.api.search('The Beatles', 'artist')
        self.assertIsNotNone(results)


class MusicBrainzTestCase(TestCase):
    """ Test the MusicBrainz API binding module
    """

    def setUp(self):
        self.brainz = MusicBrainz()

    def test_can_search_by_artist(self):
        results = self.brainz.search('The Black Keys', 'artist')
        self.assertGreater(len(results), 1)

    def test_can_get_artist(self):
        results = self.brainz.search('The Black Keys', 'artist')
        artist = self.brainz.get_artist(results['artists'][0]['id'])
        self.assertGreater(len(artist), 1)


class LastFMTestCase(TestCase):
    """ Test the LastFM API module
    """

    def setUp(self):
        self.lastfm = LastFM()
        self.brainz = MusicBrainz()

    def test_can_get_artist(self):
        search_results = self.brainz.search('The Black Keys', 'artist')
        mb_id = search_results['artists'][0]['id']
        artist = self.lastfm.get_artist_by_mbid(mb_id)
        self.assertGreater(len(artist), 1)