from rest_framework import serializers
from animais.models import Animal, Especie, Raca


ALL_FIELDS = '__all__'
class AnimalSerializer(serializers.ModelSerializer):
  sexo = serializers.SerializerMethodField()
  status = serializers.SerializerMethodField()
  raca = serializers.ReadOnlyField(source='raca.nome')
  especie = serializers.ReadOnlyField(source='raca.especie.nome')
  porte = serializers.ReadOnlyField(source='raca.porte')
  class Meta:
    model = Animal
    fields = ALL_FIELDS
    
  def get_sexo(self, obj):
    return obj.get_sexo_display()
  def get_status(self, obj):
    return obj.get_status_display()


class AnimaisDaRacaXSerializer(serializers.ModelSerializer):
  sexo = serializers.SerializerMethodField()
  status = serializers.SerializerMethodField()
  class Meta:
    model = Animal
    exclude = ['raca']
    
  def get_sexo(self, obj):
    return obj.get_sexo_display()
  def get_status(self, obj):
    return obj.get_status_display()


class EspecieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Especie
    fields = ALL_FIELDS


class RacaSerializer(serializers.ModelSerializer):
  especie = serializers.ReadOnlyField(source='especie.nome')
  porte = serializers.SerializerMethodField()
  class Meta:
    model = Raca
    fields = ALL_FIELDS
    
    