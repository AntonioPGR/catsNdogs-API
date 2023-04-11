from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from animais.models import Animal, Raca, Especie
from animais.serializers import AnimalSerializer, RacaSerializer, EspecieSerializer, AnimaisPorRacaSerializer, RacasPorEspecieSerializer


class EspeciesViewSet(ModelViewSet):
  queryset = Especie.objects.all()
  serializer_class = EspecieSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

  
class RacaViewSet(ModelViewSet):
  queryset = Raca.objects.all()
  serializer_class = RacaSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class RacasPorEspecieListView(ListAPIView):
  def get_queryset(self):
    return Raca.objects.filter(especie_id=self.kwargs['especieID'])
  serializer_class = RacasPorEspecieSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]


class AnimaisViewSet(ModelViewSet):
  queryset = Animal.objects.all()
  serializer_class = AnimalSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]


class AnimaisPorRacaListView(ListAPIView):
  def get_queryset(self):
    return Animal.objects.filter(raca_id=self.kwargs['racaID'])
  serializer_class = AnimaisPorRacaSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]