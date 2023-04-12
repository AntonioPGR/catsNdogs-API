from django.urls import path, include
from animais.views import AnimaisViewSet, RacaViewSet, EspeciesViewSet, AnimaisPorRacaListView, RacasPorEspecieListView
from rest_framework.routers import SimpleRouter


roteador_viewsets = SimpleRouter()
roteador_viewsets.register('animais', AnimaisViewSet, basename='animais')
roteador_viewsets.register('especies', EspeciesViewSet, basename='especies')
roteador_viewsets.register('racas', RacaViewSet, basename='racas')

urlpatterns = [
    path('', include(roteador_viewsets.urls)),
    path('animais/raca/<int:racaID>/', AnimaisPorRacaListView.as_view(), name='animaisDaRaca'),
    path('racas/especie/<int:especieID>/', RacasPorEspecieListView.as_view(), name='racasDaEspecie')
]