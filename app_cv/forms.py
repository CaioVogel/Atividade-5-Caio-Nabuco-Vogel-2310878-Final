from typing_extensions import Required
from django import forms
from app_cv.models import Filme
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        exclude = ["usuario"]
        fields = ['Nome', 'Icone', 'Descricao','Lancamento','Diretor','Critica_geral']
        widgets = {
          'Lancamento': forms.DateTimeInput(
        attrs={
          'type': 'date',
          'placeholder': 'Digite algo',
          'class': 'minha-classe-css'
        })
        
      }
      

class NovoUsuarioForm(UserCreationForm):
  email = forms.EmailField()
  first_name = forms.CharField(max_length=30)
  last_name = forms.CharField(max_length=30)
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email',
    'password1', 'password2']
#class BucasForm(forms.ModelForm):
  

# class AdicionarFilmes(forms.Form):
#   Nome = forms.CharField(label='Nome do filme', required = True)
#   icone = forms.URLField(label='Link da Imagem', required = True)
#   Descricao = forms.TextField(label='descricao',required = False)
#   Data = forms.DateField(label='data de lançamento',required = True)
#   Diretor = forms.CharField(label='Diretor',required = True)
#   Critica_Geral = forms.DecimalField(label='Critica entre o rotten tomatoes e IMDB',max_digits= 3, decimal_places= 1,min_value = 0,required = False)