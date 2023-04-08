from django.contrib import admin
from animais.models import Especie, Raca, Animal

class AdminEspecie(admin.ModelAdmin):
  list_display = ('nome', )
  list_display_links = ('nome', )
  search_fields = ('nome',)
  list_per_page = 20
admin.site.register(Especie, AdminEspecie)


class AdminRaca(admin.ModelAdmin):
  list_display = ('nome', 'especie', 'porte')
  list_display_links = ('nome', 'especie')
  list_filter = ('especie', 'porte',)
  search_fields = ('nome',)
  list_per_page = 20
admin.site.register(Raca, AdminRaca)

class AdminAnimal(admin.ModelAdmin):
  list_display = ('nome', 'status', 'raca', 'cidade', 'telefone_contato')
  list_display_links = ('nome', 'raca')
  list_filter = ('raca', 'cor', 'status', 'sexo')
  search_fields = ('nome',)
  list_per_page = 20
admin.site.register(Animal, AdminAnimal)