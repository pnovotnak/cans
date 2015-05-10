from django.conf.urls import url, include

from .views import LibraryView, ArtistView, ReleaseGroupView, ReleaseView

release_patterns = [
    url(r'^group/(?P<pk>\d+)', ReleaseGroupView.as_view(), name='release_group'),
    url(r'^(?P<pk>\d+)$', ReleaseView.as_view(), name='release'),
]

artist_patterns = [
    url(r'^(?P<pk>\d+)$', ArtistView.as_view(), name='artist'),
]

urlpatterns = [
    url(r'^$', LibraryView.as_view(), name='home'),

    url(r'^artist/', include(artist_patterns)),

    url(r'^release/', include(release_patterns)),
]
