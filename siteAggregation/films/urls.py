from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListFilms.as_view(), name='List-films'),
    path('', views.ListShows.as_view(), name='List-shows'),
    path('<int:pk>/', views.DetailFilms.as_view(), name='Detail-films'),
    path('<int:pk>/', views.DetailTvShows.as_view(), name='Detail-shows'),
]