from rest_framework.viewsets import ModelViewSet
from animais.models import Animal, Raca, Especie
from animais.serializers import AnimalSerializer, AnimalSerializerV2, RacaSerializer, EspecieSerializer

class BaseViewConfigs(ModelViewSet):
  pass
  


# VIEWS RENDERIZADAS: / / / / / / / / / / / / / / / / / / / / / / / / / /
class EspeciesViewSet(BaseViewConfigs):
  FIELDS = ('nome',)
  ordering_fields = FIELDS
  search_fields = FIELDS
  queryset = Especie.objects.all()
  serializer_class = EspecieSerializer
  http_method_names = ['get', 'post ']


class RacaViewSet(BaseViewConfigs):
  FIELDS = ('nome',)
  ordering_fields = FIELDS
  search_fields = FIELDS
  filterset_fields = ['porte', 'especie']
  queryset = Raca.objects.all()
  serializer_class = RacaSerializer


class AnimaisViewSet(BaseViewConfigs):
  ordering_fields = ['nome', 'cidade']
  search_fields = ['nome', 'telefone_contato', 'cidade']
  filterset_fields = ['sexo', 'cor', 'status', 'raca']
  queryset = Animal.objects.all()
  def get_serializer_class(self):
    if self.request.version == 'v2':
      return AnimalSerializerV2
    return AnimalSerializer
