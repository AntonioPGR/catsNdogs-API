from rest_framework import serializers
from animais.models import Animal, Especie, Raca
from animais.validators import Validator


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
  
  def validate(self, data_formulario):
    self.achar_e_reportar_erro_de_dados(data_formulario)
    return data_formulario
  
  def achar_e_reportar_erro_de_dados(self, data_formulario):
    if not Validator.esta_idade_correta(data_formulario['idade']):
      raise serializers.ValidationError({
        'idade':"A idade deve estar entre 0 e 100 anos!"
      })
    if not Validator.esta_cidade_correta(data_formulario['cidade']):
      raise serializers.ValidationError({
        "cidade": "Insira apenas o nome da cidade, sem numeros e/ou caracteres especiais!"
      })
    if not Validator.esta_data_de_entrada_correta(data_formulario['data_entrada']):
      raise serializers.ValidationError({
        "data_entrada": "A data de entrada no centro de resgate não pode ser no futuro!"
      })
    if not Validator.esta_telefone_correta(data_formulario['telefone']):
      raise serializers.ValidationError({
        "telefone": "O telefone deve conter 11 digitos"
      })

class AnimaisPorRacaSerializer(AnimalSerializer):
  raca = None
  class Meta(AnimalSerializer.Meta):
    exclude = ['raca']

