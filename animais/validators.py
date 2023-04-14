from datetime import datetime, timedelta
import re
from rest_framework.serializers import ValidationError


class AnimalValidador:
  @staticmethod
  def validar_idade(idade):
    if not ValidadorDeFormularios.idade_valido(idade):
      raise ValidationError({
        'idade':"A idade deve estar entre 0 e 100 anos!"
      })
  
  @staticmethod
  def validar_cidade(cidade):
    if not ValidadorDeFormularios.cidade_valido(cidade):
      raise ValidationError({
        "cidade": "Insira apenas o nome da cidade, sem numeros e/ou caracteres especiais!"
      })
  
  @staticmethod
  def validar_data_de_entrada(data):
    if not ValidadorDeFormularios.data_de_entrada_valido(data):
      raise ValidationError({
        "data_entrada": "A data de entrada no centro de resgate não pode ser no futuro!"
      })
      
  @staticmethod
  def validar_telefone_contato(telefone):
    if not ValidadorDeFormularios.telefone_valido(telefone):
      raise ValidationError({
        "telefone_contato": "O telefone deve estar no formato: xx 9xxxx-xxxx"
      })

class ValidadorDeFormularios:
  @staticmethod
  def idade_valido(idade):
    return idade >= 0 and idade <= 100
  
  @staticmethod
  def cidade_valido(cidade):
    return cidade.replace(' ', '').isalpha()
  
  @staticmethod
  def data_de_entrada_valido(data_entrada):
    return data_entrada < datetime.date(datetime.now() + timedelta(days=1))

  @staticmethod
  def telefone_valido(telefone):
    """XX 9XXXX-XXXX"""
    modelo = '\d{2} 9\d{4}-\d{4}'
    return re.findall(modelo, telefone)
  