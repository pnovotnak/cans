from django.conf.urls import url, include

from .views import LibraryView, ArtistView, ReleaseGroupView, ReleaseView

release_group_patterns = [
    url(r'^(?P<pk>\d+)', ReleaseGroupView.as_view(), name='detail'),
]

release_patterns = [
    url(r'^group/', include(release_group_patterns, namespace='group')),

    url(r'^(?P<pk>\d+)$', ReleaseView.as_view(), name='detail'),
]

artist_patterns = [
    url(r'^(?P<pk>\d+)$', ArtistView.as_view(), name='detail'),
]

urlpatterns = [
    url(r'^$', LibraryView.as_view(), name='home'),

    url(r'^artist/', include(artist_patterns, namespace='artist')),

    url(r'^release/', include(release_patterns, namespace='release')),
]
