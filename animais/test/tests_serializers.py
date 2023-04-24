from django.test import TestCase
from animais.serializers import AnimalSerializer
from animais.test.default_instances import animal_default


class AnimalSerializerTestCase(TestCase):
  
  def setUp(self):
    self.animal = animal_default
    self.serializer = AnimalSerializer(instance=self.animal)
    self.serializer_data = self.serializer.data
    
  def test_verificar_campos_serializados(self):
    self.assertEqual(
      set(self.serializer_data.keys()),
      set(['id', 'nome', 'sexo', 'cor', 'idade', 'cidade', 'data_entrada', 'descricao', 'telefone_contato', 'status', 'foto', 'raca'])
    )
    
  def test_verificar_dados_do_serializador(self):
    self.assertEqual(self.serializer_data['nome'], self.animal.nome)
    self.assertEqual(self.serializer_data['sexo'], self.animal.sexo)
    self.assertEqual(self.serializer_data['cor'], self.animal.cor)
    self.assertEqual(self.serializer_data['idade'], self.animal.idade)
    self.assertEqual(self.serializer_data['cidade'], self.animal.cidade)
    self.assertEqual(self.serializer_data['data_entrada'], self.animal.data_entrada)
    self.assertEqual(self.serializer_data['descricao'], self.animal.descricao)
    self.assertEqual(self.serializer_data['telefone_contato'], self.animal.telefone_contato)
    self.assertEqual(self.serializer_data['status'], self.animal.status)
    self.assertEqual(self.serializer_data['foto'], self.animal.foto.url)
  #   self.assertEqual(self.serializer_data['raca'], self.serializer.to_representation(self.animal.raca))