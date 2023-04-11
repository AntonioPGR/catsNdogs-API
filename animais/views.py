from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from animais.models import Animal, Raca, Especie
from animais.serializers import AnimalSerializer, RacaSerializer, EspecieSerializer, AnimaisDaRacaXSerializer


class AnimaisViewSet(ModelViewSet):
  queryset = Animal.objects.all()
  serializer_class = AnimalSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]


class AnimaisDaRacaXListView(ListAPIView):
  def get_queryset(self):
    return Animal.objects.filter(raca_id=self.kwargs['racaID'])
  serializer_class = AnimaisDaRacaXSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]


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
