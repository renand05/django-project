from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonViewSet(viewsets.ViewSet):
    def list(self, request):
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PokemonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        pokemon = Pokemon.objects.get(id=pk)
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
