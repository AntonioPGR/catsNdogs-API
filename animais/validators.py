from datetime import datetime

class Validator:
  
  @staticmethod
  def esta_idade_correta(idade):
    return idade >= 0 and idade <= 100
  
  @staticmethod
  def esta_cidade_correta(cidade):
    return cidade.replace(' ', '').isalpha()
  
  @staticmethod
  def esta_data_de_entrada_correta(data_entrada):
    return data_entrada < datetime.date(datetime.now())

  @staticmethod
  def esta_telefone_correta(telefone):
    return len(telefone) == 11