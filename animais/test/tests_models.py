from django.test import TestCase
from animais.test.default_instances import animal_default, raca_default

class AnimalModelTestCase(TestCase):
  
  def setUp(self):
    self.animal = animal_default
    
  def test_criar_novo_animal_com_props_default(self):
    self.assertEqual(self.animal.nome, 'Bob')
    self.assertEqual(self.animal.idade,10)
    self.assertEqual(self.animal.cidade,'Pocos de Caldas')
    self.assertEqual(self.animal.data_entrada,'2023-04-20')
    self.assertEqual(self.animal.descricao,'descricao')
    self.assertEqual(self.animal.telefone_contato,'35 99148-9037')
    self.assertEqual(self.animal.sexo , 'M')
    self.assertEqual(self.animal.cor , 'preto')
    self.assertEqual(self.animal.status , 'D')
    self.assertEqual(self.animal.raca, raca_default)
    