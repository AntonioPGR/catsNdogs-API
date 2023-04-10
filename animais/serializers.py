from rest_framework import serializers
from animais.models import Animal, Especie, Raca


ALL_FIELDS = '__all__'
class AnimalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Animal
    fields = ALL_FIELDS
    

class EspecieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Especie
    fields = ALL_FIELDS


class RacaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Raca
    fields = ALL_FIELDS
    