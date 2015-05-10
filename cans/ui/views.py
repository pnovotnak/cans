from django.views.generic import ListView, DetailView

from data.models import Artist, ReleaseGroup, Release


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


class ReleaseGroupView(ListView):

    model = ReleaseGroup

    def get_context_data(self, **kwargs):
        context = super(ReleaseGroupView, self).get_context_data(**kwargs)

        # Add title
        context['page_name'] = self.object.name
        return context


class ReleaseView(DetailView):

    template_name = 'ui/release/detail.html'
    model = Release

    def get_context_data(self, **kwargs):
        context = super(ReleaseView, self).get_context_data(**kwargs)

        # Add title
        context['page_name'] = self.object.name
        return context
