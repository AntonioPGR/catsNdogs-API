from django.db import models
from django.core.validators import MaxValueValidator

class Especies(models.Model):
  nome = models.CharField(max_length=30, null=False, blank=False)
  

porte = (
  ("P", 'Pequeno'),
  ("M", "Médio"),
  ("G", "Grande")
)
class Raca(models.Model):
  nome = models.CharField(max_length=30, null=False, blank=False)
  especie = models.ForeignKey(Especies, on_delete=models.CASCADE, null=False, blank=False)
  porte = models.CharField(max_length=1, choices=porte, blank=False, null=False)
  

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
  nome = models.CharField(max_length=30, null=False, blank=False)
  sexo = models.CharField(max_length=1, choices=opcoes_sexo, null=False, blank=False)
  cor = models.CharField(max_length=10, choices=opcoes_cores, null=False, blank=False)
  idade = models.PositiveIntegerField(validators=[MaxValueValidator(99)],null=False, blank=False)
  cidade = models.CharField(max_length=30, blank=True, null=True)
  data_entrada = models.DateField(blank=True, null=True)
  descricao = models.TextField(max_length=2000, blank=False, null=False)
  telefone_contato = models.CharField(max_length=13, blank=True, null=True)
  status = models.CharField(max_length=1, choices=opcoes_status, blank=False, null=False)
  foto = models.ImageField(upload_to="Animais/%Y/%m/%d", null=False, blank=False)
  
  