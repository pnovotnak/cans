from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from data.models import Artist, ReleaseGroup, Release
from .forms import SearchForm

from django.core.urlresolvers import reverse


class LibraryView(ListView):
    """ An index view for your library.
    """

    template_name = 'ui/artist/list.html'
    model = Artist

    def get_context_data(self, **kwargs):
        context = super(LibraryView, self).get_context_data(**kwargs)

        # Add title
        context['title'] = 'Library'
        return context


class ArtistView(DetailView):
    """ Artist view. Show artist info and their material.
    """

    template_name = 'ui/artist/detail.html'
    model = Artist

    def get_context_data(self, **kwargs):
        context = super(ArtistView, self).get_context_data(**kwargs)

        # Add title
        context['page_name'] = self.object.name
        return context


class ReleaseGroupView(DetailView):
    """ The logical child of the ArtistView.

    Show a list of releases in a release group.
    """

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
    """ Show details about a release.
    """

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


class SearchView(FormView):
    """ A view that shows search results.

    Since we have a search bar in the header, we don't need to include it on the page.
    """

    template_name = 'ui/search/results.html'
    form_class = SearchForm

    def form_valid(self, form):
        return super(SearchView, self).form_valid(form)
