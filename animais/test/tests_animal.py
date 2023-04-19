from rest_framework.test import APITestCase
from animais.models import Animal
from django.urls import reverse

class AnimalTestCase(APITestCase):
  
  def setUp(self):
    self.list_url = reverse('Animais-list')