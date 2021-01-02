from rest_framework import viewsets
from rest_framework.response import Response

from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonViewSet(viewsets.ViewSet):
    def list(self, request):
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
