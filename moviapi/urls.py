from django.urls import path
from .views import MovieListView, MovieDetailView
from . import views

urlpatterns = [
    path('', MovieListView.as_view(), name='moviapi-home'),
    path('about/', views.about, name='moviapi-about'),
    path('movie/index=<int:pk>/', MovieDetailView.as_view(), name='moviapi-detail'),
]
