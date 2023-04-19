from rest_framework.test import APITestCase
from django.urls import reverse
from animais.models import Raca

class RacaTestCase(APITestCase):
  
  def setUp(self):
    self.list_url = reverse('Racas-list')