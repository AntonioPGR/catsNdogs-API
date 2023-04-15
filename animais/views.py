from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from animais.models import Animal, Raca, Especie
from animais.serializers import AnimalSerializer, RacaSerializer, EspecieSerializer, AnimaisPorRacaSerializer, RacasPorEspecieSerializer

class BaseViewConfigs:
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
  filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
  
class BaseViewSet(BaseViewConfigs, ModelViewSet):
  pass
  

class BaseListView(BaseViewConfigs, ListAPIView):
  pass


# VIEWS RENDERIZADAS: / / / / / / / / / / / / / / / / / / / / / / / / / /
class BaseEspeciesViews():
  FIELDS = ('nome',)
  ordering_fields = FIELDS
  search_fields = FIELDS
class EspeciesViewSet(BaseViewSet, BaseEspeciesViews):
  queryset = Especie.objects.all()
  serializer_class = EspecieSerializer


class BaseRacasViews():
  FIELDS = ('nome',)
  ordering_fields = FIELDS
  search_fields = FIELDS
  filterset_fields = ['porte', 'especie']
class RacaViewSet(BaseViewSet, BaseRacasViews):
  queryset = Raca.objects.all()
  serializer_class = RacaSerializer


class BaseAnimaisViews():
  ordering_fields = ['nome', 'cidade']
  search_fields = ['nome', 'telefone_contato', 'cidade']
  filterset_fields = ['sexo', 'cor', 'status', 'raca']
class AnimaisViewSet(BaseViewSet, BaseAnimaisViews):
  queryset = Animal.objects.all()
  serializer_class = AnimalSerializer