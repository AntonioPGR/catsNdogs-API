from rest_framework import serializers
from animais.models import Animal, Especie, Raca
from animais.validators import AnimalValidador


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
    

class AnimalSerializer(serializers.ModelSerializer):  
  class Meta:
    model = Animal
    exclude = NO_FIELDS
    read_only_fields = ('id',)
  
  def validate(self, data_formulario):
    AnimalValidador.validar_idade(data_formulario['idade'])
    AnimalValidador.validar_cidade(data_formulario['cidade'])
    AnimalValidador.validar_data_de_entrada(data_formulario['data_entrada'])
    AnimalValidador.validar_telefone_contato(data_formulario['telefone_contato'])
    return data_formulario
class AnimalSerializerV2(AnimalSerializer):
  class Meta(AnimalSerializer.Meta):
    exclude = ['cidade', 'telefone_contato']

