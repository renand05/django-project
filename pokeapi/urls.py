from django.urls import path
from .views import PokemonViewSet
from . import views

urlpatterns = [
    path('pokemons', PokemonViewSet.as_view({
        'get': 'list',
        'post': 'create'
        })),
    path('pokemon/<str:pk>', PokemonViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
        }))
]
