from rest_framework import viewsets
from animais.models import Animal, Raca, Especie
from animais.serializers import AnimalSerializer, RacaSerializer, EspecieSerializer


class AnimaisViewSet(viewsets.ModelViewSet):
  """Exibet todos os animais salvos no banco de dados"""
  queryset = Animal.objects.all()
  serializer_class = AnimalSerializer


class EspeciesViewSet(viewsets.ModelViewSet):
  """Exibe todos as espécies salvas no banco de dados"""
  queryset = Especie.objects.all()
  serializer_class = EspecieSerializer
  
  
class RacaViewSet(viewsets.ModelViewSet):
  """Exibe todos as raças salvas no banco de dados"""
  queryset = Raca.objects.all()
  serializer_class = RacaSerializer
