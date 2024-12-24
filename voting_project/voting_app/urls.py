from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movies, name='movies'),
    path('vote/<int:movie_id>/', views.vote, name='vote'),
    path('ratings/', views.ratings, name='ratings'),
    path('series/', views.series, name='series'),
    path('vote_series/<int:series_id>/', views.vote_series, name='vote_series'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

