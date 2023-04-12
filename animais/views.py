from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from animais.models import Animal, Raca, Especie
from animais.serializers import AnimalSerializer, RacaSerializer, EspecieSerializer, AnimaisPorRacaSerializer, RacasPorEspecieSerializer

class BaseAuthConfigs:
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
  
  
class BaseViewSet(BaseAuthConfigs, ModelViewSet):
  pass
  

class BaseListView(BaseAuthConfigs, ListAPIView):
  pass


# VIEWS RENDERIZADAS: / / / / / / / / / / / / / / / / / / / / / / / / / /
class EspeciesViewSet(BaseViewSet):
  queryset = Especie.objects.all()
  serializer_class = EspecieSerializer

  
class RacaViewSet(BaseViewSet):
  queryset = Raca.objects.all()
  serializer_class = RacaSerializer

class RacasPorEspecieListView(BaseListView):
  serializer_class = RacasPorEspecieSerializer
  def get_queryset(self):
    return Raca.objects.filter(especie_id=self.kwargs['especieID'])


class AnimaisViewSet(BaseViewSet):
  queryset = Animal.objects.all()
  serializer_class = AnimalSerializer


class AnimaisPorRacaListView(BaseListView):
  serializer_class = AnimaisPorRacaSerializer
  def get_queryset(self):
    return Animal.objects.filter(raca_id=self.kwargs['racaID'])