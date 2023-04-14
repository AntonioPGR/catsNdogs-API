from rest_framework import serializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from animais.models import Animal, Especie, Raca


ALL_FIELDS = '__all__'
NO_FIELDS = []
class EspecieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Especie
    fields = ALL_FIELDS


class RacaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Raca
    exclude = NO_FIELDS
  
    
class RacasPorEspecieSerializer(RacaSerializer):
  especie = None
  class Meta(RacaSerializer.Meta):
    exclude = ['especie']
    

class AnimalSerializer(serializers.ModelSerializer):  
  class Meta:
    model = Animal
    exclude = NO_FIELDS
    read_only_fields = ('id',)


class AnimaisPorRacaSerializer(AnimalSerializer):
  raca = None
  class Meta(AnimalSerializer.Meta):
    exclude = ['raca']

