from django.urls import path, include
from animais.views import AnimaisViewSet, RacaViewSet, EspeciesViewSet
from rest_framework.routers import DefaultRouter


roteador_viewsets = DefaultRouter()
roteador_viewsets.register(r'animais/(?P<version>(v1|v2))', AnimaisViewSet, basename='animais')
roteador_viewsets.register('especies', EspeciesViewSet, basename='especies')
roteador_viewsets.register('racas', RacaViewSet, basename='racas')

urlpatterns = [
    path('', include(roteador_viewsets.urls)),
]