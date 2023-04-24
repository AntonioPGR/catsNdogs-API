from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse


class AutenticacaoDeUsuarioTestCase(APITestCase):
  
  usernameCorreto = 'usuario1'
  passwordCorreto = '12345'
  usernameIncorreto = 'usuario12345'
  passwordIncorreto = '1234'
  
  def setUp(self):
    self.list_url = reverse('Especies-list')
    self.user = User.objects.create_user(self.usernameCorreto, password=self.passwordCorreto)
    
  def test_authenticacao_user_com_credenciais_corretas(self):
    user = authenticate(username=self.usernameCorreto, password=self.passwordCorreto)
    self.assertTrue(user.is_authenticated)
  
  def test_authenticacao_user_com_nome_incorretas(self):
    user = authenticate(username=self.usernameIncorreto, password=self.passwordCorreto)
    self.assertTrue(user is None)
    
  def test_authenticacao_user_com_senha_incorreta(self):
    user = authenticate(username=self.usernameCorreto, password=self.passwordIncorreto)
    self.assertTrue(user is None)
  
  def test_authenticacao_user_com_credenciais_incorretas(self):
    user = authenticate(username=self.usernameIncorreto, password=self.passwordIncorreto)
    self.assertTrue(user is None)