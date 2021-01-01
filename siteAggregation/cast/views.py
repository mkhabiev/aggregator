from django.views.generic import ListView, DetailView

from cast.models import Cast, TVActor

class CastView(ListView):
    template_name = 'cast/index_cast.html'

    def get_queryset(self):
        return Cast.objects.all()


class CastDetailView(DetailView):
    model = Cast
    template_name = 'cast/detail_cast.html'


class TvActorView(ListView):
    template_name = 'cast/index_tvactor.html'

    def get_queryset(self):
        return TVActor.objects.all()


class TvActorDetailView(DetailView):
    model = TVActor
    template_name = 'cast/detail_tvactor.html'