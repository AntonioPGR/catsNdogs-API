from animais.models import Animal, Raca, Especie

especie_default = Especie(
  nome='especie1'
)

raca_default = Raca(
  especie=especie_default,
  nome='raca1',
)

animal_default = Animal(
  nome='Bob',
  idade=10,
  cidade='Pocos de Caldas',
  data_entrada='2023-04-20',
  descricao='descricao',
  telefone_contato='35 99148-9037',
  raca=raca_default
)