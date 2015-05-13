from django.core.management.base import BaseCommand, CommandError

from data.api import API

from data.models import Artist, ReleaseGroup, Release

class Command(BaseCommand):
    help = 'Gets artist images'

    def add_arguments(self, parser):
        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        api = API()
        for artist in Artist.object.filter(image=None):

            artist_detail = api.lastfm.get_artist_by_mbid(artist.mbid)
            """
            url = artist_detail['image']
            image = save_image(url)
            artist(image=image)
            artist.save()
            """
