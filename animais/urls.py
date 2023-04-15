from django.urls import path, include
from animais.views import AnimaisViewSet, RacaViewSet, EspeciesViewSet
from rest_framework.routers import SimpleRouter, DefaultRouter


roteador_viewsets = SimpleRouter()
roteador_viewsets.register('animais', AnimaisViewSet, basename='animais')
roteador_viewsets.register('especies', EspeciesViewSet, basename='especies')
roteador_viewsets.register('racas', RacaViewSet, basename='racas')

urlpatterns = [
    path('', include(roteador_viewsets.urls)),
]