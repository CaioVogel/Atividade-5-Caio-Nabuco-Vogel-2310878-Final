from django.contrib import admin
from .models import Filme, Links

# Register your models here.
class FilmeAdmin(admin.ModelAdmin):
  list_display = ['Nome','Lancamento','Diretor','Critica_geral']
  ordering = ['Critica_geral']

admin.site.register(Filme, FilmeAdmin)

class LinkAdmin(admin.ModelAdmin):
  list_display = ['FK_NomeF','nomeL','Critica']

admin.site.register(Links, LinkAdmin)
