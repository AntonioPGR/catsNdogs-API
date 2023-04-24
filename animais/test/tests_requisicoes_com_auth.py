from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from animais.models import Especie
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import authenticate

class RequisicoesParaEspecieComAutenticacaoTestCase(APITestCase):
  
  username = 'usuario1'
  password = '1234'
  
  def setUp(self):
    self.list_url = reverse('Especies-list')
    self.especie_1 = Especie.objects.create(nome='especieTeste1')
    self.especie_2 = Especie.objects.create(nome='especieTeste2')
    self.user = User.objects.create_user(username=self.username, password=self.password)
  
  def autenticar_usuario(self):
    self.client.force_authenticate(self.user)
  
  def test_requisicao_get_para_listar_especies_com_autenticacao(self):
    self.autenticar_usuario()
    response = self.client.get(self.list_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  # def test_requisicao_post_para_adicionar_especie_com_autenticacao(self):
  #   self.autenticar_usuario()
  #   response = self.client.post(self.list_url, data={})
  #   self.assertEqual(response.status_code, status.HTTP_201_CREATED)
  
  # def test_requisicao_put_para_modificar_especie_com_autenticacao(self):
  #   self.autenticar_usuario()
  #   response = self.client.put('/especies/1/', data={
  #     "nome": 'especietesteModify'
  #   })
  #   self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
  # def test_requisicao_delete_para_deletar_especie_com_autenticacao(self):
  #   self.autenticar_usuario()
  #   response = self.client.delete('/especies/1/')
  #   self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)