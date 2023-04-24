from rest_framework.viewsets import ModelViewSet
from animais.models import Animal, Raca, Especie
from animais.serializers import AnimalSerializer, AnimalSerializerV2, RacaSerializer, EspecieSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class BaseViewConfigs(ModelViewSet):
  def create(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()
      response = Response(serializer.data, status=HTTP_201_CREATED)
      id = str(serializer.data['id'])
      response['location'] = request.build_absolute_uri() + id
      return response


# VIEWS RENDERIZADAS: / / / / / / / / / / / / / / / / / / / / / / / / / /
class EspeciesViewSet(BaseViewConfigs):
  FIELDS = ('nome',)
  ordering_fields = FIELDS
  search_fields = FIELDS
  queryset = Especie.objects.all()
  serializer_class = EspecieSerializer
  http_method_names = ['get', 'post']

  #CACHE
  @method_decorator(cache_page(30))
  def dispatch(self, *args, **kwargs):
    return super(EspeciesViewSet, self).dispatch(*args, **kwargs)

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