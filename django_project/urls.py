"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_cv import views

urlpatterns = [
    path('',views.inicio),
    path('login', views.login_usuario),
    path('logout',views.logout_usuario),
    path('cadastrar', views.cadastro_usuario),
    path('home', views.index),
    path('Adicionar', views.Adicionar),
    path('Editar/<str:nome>/',views.Editar, name='editar_filme'),
    path('Remover/<str:nome>/',views.Remover, name='remover_filme'),
    path('admin/', admin.site.urls),
]
