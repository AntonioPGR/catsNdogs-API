import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from animais.models import Animal, opcoes_cores, opcoes_sexo, opcoes_status, Raca
from random import randint


def popular_animais(numero_de_animais:int):
  fake_generator = Faker('pt_BR')
  Faker.seed(10329848923742830)
  for _ in range(numero_de_animais):
    animal = criar_animal_falso(fake_generator)
    animal.save()
  
  
def criar_animal_falso(fake_generator):
  nome = fake_generator.name()
  sexo = fake_generator.random_element(elements=tupla_para_range(opcoes_sexo))
  cor = fake_generator.random_element(elements=tupla_para_range(opcoes_cores))
  idade = randint(1, 40)
  cidade = fake_generator.city()
  data_entrada = fake_generator.date()
  descricao = fake_generator.text()
  telefone_contato = "{} 9{}-{}".format(randint(10, 99), randint(1000, 9999), randint(1000, 9999))
  status = fake_generator.random_element(elements=tupla_para_range(opcoes_status))
  foto = "Animais\/2023/04/13/doguinho.jpg"
  raca = Raca.objects.order_by('?').first()
  return Animal(
    nome=nome, 
    sexo=sexo, 
    cor=cor, 
    idade=idade, 
    cidade=cidade, 
    data_entrada=data_entrada, 
    descricao=descricao, 
    telefone_contato=telefone_contato, 
    status=status, 
    foto=foto,
    raca = raca
  )


def tupla_para_range(tupla_opcoes:tuple):
  return range(len(tupla_opcoes))

# Animal.objects.all().delete()
popular_animais(15)
print('sucesso!')