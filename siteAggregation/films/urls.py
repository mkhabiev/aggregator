from django.urls import path
from .views import ListFilms, TvShowView, DetailFilms, DetailTvShows
from . import views

urlpatterns = [
    #path('', views.ListFilms.as_view(), name='List-films'),
    #path('', views.ListShows.as_view(), name='List-shows'),
    #path('<int:pk>/', views.DetailFilms.as_view(), name='Detail-films'),
    #path('<int:pk>/', views.DetailTvShows.as_view(), name='Detail-shows'),
    path('films/', ListFilms.as_view()),
    path('films/<int:pk>/', DetailFilms.as_view()),
    path('shows/', TvShowView.as_view()),
    path('shows/<int:pk>/', DetailTvShows.as_view()),
]