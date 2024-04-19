from django.shortcuts import render, redirect
from .models import Filme,Links
from .forms import FilmeForm, NovoUsuarioForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def inicio(request):
  return render (request, 'inicio.html')

def login_usuario(request):
 formulario = AuthenticationForm()
 if request.method == 'POST' and request.POST:
  formulario = AuthenticationForm(request, request.POST)
  if formulario.is_valid():
    usuario = formulario.get_user()
    login(request, usuario)
    return redirect('/home')
 return render(request, 'login.html', {'formulario': formulario})

def cadastro_usuario(request):
 formulario = NovoUsuarioForm()
 if request.method == 'POST' and request.POST:
  formulario = NovoUsuarioForm(request.POST)
  if formulario.is_valid():
    novo_usuario = formulario.save(commit=False)
    novo_usuario.email = formulario.cleaned_data['email']
    novo_usuario.first_name = formulario.cleaned_data['first_name']
    novo_usuario.last_name = formulario.cleaned_data['last_name']
    novo_usuario.save()
    return redirect('/login')
 return render(request,'cadastro_usuario.html',
 {'formulario': formulario})


def logout_usuario(request):
  logout(request)
  return redirect('/')


@login_required
def index(request):
  filmes = Filme.objects.filter(usuario=request.user).all()
  links = Links.objects.all()
  
  return render(request,"index.html",{'filmes': filmes,'links':links})

@login_required
def Adicionar(request):
  formulario = FilmeForm()
  if request.method == 'POST' and request.POST:
    formulario = FilmeForm(request.POST)
    if formulario.is_valid():
      nova_referencia = formulario.save(commit=False)
      nova_referencia.usuario = request.user
      nova_referencia.save()
      return redirect("/home")
  return render(request,"Adicionar_Dado.html",{'formulario': formulario}) 

@login_required
def Editar(request, nome):
  filme = get_object_or_404(Filme, Nome=nome, usuario=request.user) 
  formulario = FilmeForm(instance=filme)
  if request.method == 'POST' and request.POST:
    formulario = FilmeForm(request.POST,instance=filme)
    if formulario.is_valid():
      formulario.save()
      return redirect("/home")
  return render(request,"Editar_Dado.html",{'formulario':formulario}) 

@login_required
def Remover(request, nome):
  filme = get_object_or_404(Filme, Nome=nome,usuario=request.user) 
  if request.method == 'POST' and request.POST:
    filme.delete()
    return redirect("/home")
  return render(request, "Remover_Dado.html", {'filme':filme})

#def pesquisa(request):
#fomulario = BuscaForm()
#if request.method == 'GET' and request.GET:
#formulario = BuscaForm(request.GET)
#if formulario.is_valid():
#formulario.save()
#return redirect("/")
#return render(request, "Pesquisar_Dado.html",{'formulario':formulario})
