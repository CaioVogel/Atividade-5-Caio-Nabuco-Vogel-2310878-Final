from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Filme(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  Nome = models.CharField(max_length = 80)
  Icone = models.CharField(max_length = 2000)
  Descricao = models.TextField(blank=True)
  Lancamento = models.DateField()
  Diretor= models.CharField(max_length = 80)
  Critica_geral = models.DecimalField(max_digits= 3, decimal_places= 1)

  def __str__ (self):
    return self.Nome


class Links(models.Model):
  OPTIONS = [
    ("R","Rotten tomatoes"),
    ("I","IMDB"),  
  ]
  nomeL = models.CharField(max_length = 1, choices = OPTIONS)
  link = models.URLField(max_length = 2000)
  FK_NomeF = models.CharField(max_length = 80)
  Critica = models.DecimalField(max_digits= 3, decimal_places= 1)
  QTDCritical = models.CharField(max_length = 10)
  
  def __str__ (self):
    return self.nomeL