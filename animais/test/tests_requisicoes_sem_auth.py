from rest_framework.test import APITestCase
from animais.models import Especie
from django.urls import reverse
from rest_framework import status

class RequisicoesParaEspecieSemAutenticacaoTestCase(APITestCase):
  
  def setUp(self):
    self.list_url = reverse('Especies-list')
    self.especie_1 = Especie.objects.create(nome='especieTeste1')
    self.especie_2 = Especie.objects.create(nome='especieTeste2')
  
  def test_requisicao_get_para_listar_especies_sem_autenticacao(self):
    response = self.client.get(self.list_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  def test_requisicao_post_para_adicionar_especie_sem_autenticacao(self):
    response = self.client.post(self.list_url, data={
      "nome": 'especieteste3'
    })
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
  
  def test_requisicao_put_para_modificar_especie_sem_autenticacao(self):
    response = self.client.put('/especies/1/', data={
      "nome": 'especietesteModify'
    })
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
  def test_requisicao_delete_para_deletar_especie_sem_autenticacao(self):
    response = self.client.delete('/especies/1/')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)