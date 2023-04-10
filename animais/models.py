from django.db import models
from django.core.validators import MaxValueValidator

class Especie(models.Model):
  nome = models.CharField(verbose_name="Nome", max_length=30, null=False, blank=False)
  
  def __str__(self) -> str:
    return self.nome
  

porte = (
  ("P", 'Pequeno'),
  ("M", "Médio"),
  ("G", "Grande")
)
class Raca(models.Model):
  nome = models.CharField(verbose_name="Nome", max_length=30, null=False, blank=False)
  especie = models.ForeignKey(Especie, verbose_name="Espécie", on_delete=models.CASCADE, null=False, blank=False)
  porte = models.CharField(max_length=1, verbose_name="Porte", choices=porte, blank=False, null=False)
  
  def __str__(self) -> str:
    return self.nome


opcoes_sexo = (
  ("M", "Masculino"),
  ("F", "Feminino"),
)
opcoes_cores = (
  ("preto", "Preto"),
  ("branco", "Branco"),
  ("cinza", "Cinza"),
  ("marrom", "Marrom"),
  ("caramelo", "Caramelo"),
)
opcoes_status = (
  ("D", "Disponivel para adoção"),
  ("A", "Adoção em Andamento"),
  ("F", "Adoção finalizada"),
)
class Animal(models.Model):
  nome = models.CharField(max_length=30, verbose_name="Nome", null=False, blank=False)
  sexo = models.CharField(max_length=1, verbose_name="Sexo", choices=opcoes_sexo, null=False, blank=False)
  cor = models.CharField(max_length=10, verbose_name="Cor", choices=opcoes_cores, null=False, blank=False)
  idade = models.PositiveIntegerField(validators=[MaxValueValidator(99)], verbose_name="Idade", null=False, blank=False)
  cidade = models.CharField(max_length=30, verbose_name="Cidade", blank=True, null=True)
  data_entrada = models.DateField(verbose_name="Data de entrada no abrigo", blank=True, null=True)
  descricao = models.TextField(max_length=2000, verbose_name="Descrição da história do animal", blank=False, null=False)
  telefone_contato = models.CharField(max_length=13, verbose_name="Telefone para contato", blank=True, null=True)
  status = models.CharField(max_length=1, verbose_name="Status de adoção", choices=opcoes_status, blank=False, null=False)
  foto = models.ImageField(upload_to="Animais/%Y/%m/%d", verbose_name="Foto do animal", null=False, blank=False)
  raca = models.ForeignKey(Raca, on_delete=models.SET_NULL, blank=True, null=True)
  
  def __str__(self) -> str:
    return self.nome
  