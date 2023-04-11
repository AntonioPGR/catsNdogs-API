from rest_framework import serializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from animais.models import Animal, Especie, Raca


ALL_FIELDS = '__all__'
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
    
  def get_porte(self, obj):
    return obj.get_porte_display()
  
    
class RacasPorEspecieSerializer(serializers.ModelSerializer):
  porte = serializers.SerializerMethodField()
  class Meta:
    model = Raca
    exclude = ['especie']
  
  def get_porte(self, obj):
    return obj.get_porte_display()
    

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


class AnimaisPorRacaSerializer(serializers.ModelSerializer):
  sexo = serializers.SerializerMethodField()
  status = serializers.SerializerMethodField()
  class Meta:
    model = Animal
    exclude = ['raca']
    
  def get_sexo(self, obj):
    return obj.get_sexo_display()
  def get_status(self, obj):
    return obj.get_status_display()

