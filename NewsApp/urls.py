from os import name
from django.urls import path
from django.urls.conf import include
from .views import index, sports, politics, movies

urlpatterns = [
    path('', index, name='Index'),
    path('sports/', sports, name="Movies"),
    path('politics/', politics, name="Politics"),
    path('movies/', movies, name="Movies"),
]
