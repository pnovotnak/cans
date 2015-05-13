from django.views.generic import ListView, DetailView

from data.models import Artist, ReleaseGroup, Release

from django.core.urlresolvers import reverse


class LibraryView(ListView):

    template_name = 'ui/artist/list.html'
    model = Artist

    def get_context_data(self, **kwargs):
        context = super(LibraryView, self).get_context_data(**kwargs)

        # Add title
        context['title'] = 'Library'
        return context


class ArtistView(DetailView):

    template_name = 'ui/artist/detail.html'
    model = Artist

    def get_context_data(self, **kwargs):
        context = super(ArtistView, self).get_context_data(**kwargs)

        # Add title
        context['page_name'] = self.object.name
        return context


class ReleaseGroupView(DetailView):

    template_name = 'ui/release/list.html'
    model = ReleaseGroup

    def get_context_data(self, **kwargs):
        context = super(ReleaseGroupView, self).get_context_data(**kwargs)

        # Add title
        context['page_name'] = self.object.name
        context['breadcrumb'] = [
            {
                'text': self.object.artist.name,
                'href': reverse('ui:artist:detail', args=[self.object.artist.pk])
            }
        ]
        return context


class ReleaseView(DetailView):

    template_name = 'ui/release/detail.html'
    model = Release

    def get_context_data(self, **kwargs):
        context = super(ReleaseView, self).get_context_data(**kwargs)

        # Add title
        context['page_name'] = self.object.name
        context['breadcrumb'] = [
            {
                'text': self.object.release_group.artist.name,
                'href': reverse('ui:artist:detail', args=[self.object.release_group.artist.pk])
            },
            {
                'text': self.object.release_group.name,
                'href': reverse('ui:release:group:detail', args=[self.object.release_group.pk])
            }
        ]
        return context


class SearchView(ListView):

    template_name = 'ui/search/results.html'

    def get_queryset(self, request):
        