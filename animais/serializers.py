from rest_framework import serializers
from animais.models import Animal, Especie, Raca


class SerializerAnimal(serializers.ModelSerializer):
  class Meta:
    model = Animal,
    fields = '__all__'
    

class SerializerEspecie(serializers.ModelSerializer):
  class Meta:
    model = Especie
    fields = '__all__'


class SerializerRaca(serializers.ModelSerializer):
  class Meta:
    model = Raca
    fields = '__all__'
    