from django.shortcuts import render
from django.views.generic import ListView, DetailView

from films.forms import CommentForm
from films.models import Film, TVShow


class ListFilms(ListView):
    """
    Listing films
    """
    model = Film
    template_name = 'films/list_films.html'


class DetailFilms(DetailView):
    """
    Details about film
    """
    model = Film
    template_name = 'films/detail_film.html'
    extra_context = {'form': CommentForm()}

    def post(self, request, *args, **kwargs):
        film_id = kwargs['pk']
        film = Film.objects.get(pk=film_id)
        form = CommentForm(request.POST, initial={'film': film})
        if form.is_valid():
            form.save()

        return self.get(request, *args, **kwargs)

class DetailTvShows(DetailView):
    """
    Details about shows
    """
    model = TVShow
    template_name = 'films/detail_show.html'
    extra_context = {'form': CommentForm()}

    def post(self, request, *args, **kwargs):
        show_id = kwargs['pk']
        show = TVShow.objects.get(pk=show_id)
        form = CommentForm(request.POST, initial={'show': show})
        if form.is_valid():
            form.save()

        return self.get(request, *args, **kwargs)

class ListShows(ListView):
    """
    Listing shows
    """
    model = TVShow
    template_name = 'films/list_shows.html'