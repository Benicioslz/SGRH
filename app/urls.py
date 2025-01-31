from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.home, name='home'),
    path('', include('Estado.urls')),
    path('', include('Cidade.urls')),
    path('', include('Bairro.urls')),
    path('', include('Genero.urls')),
    path('', include('Endereco.urls')),
    path('', include('Pessoa.urls')),
    path('', include('Tipo_Contato.urls')),
    path('', include('Tipo_Contato_Pessoa.urls')),
    path('', include('Setor.urls')),
    path('', include('Cargo.urls')),
    path('', include('Lotacao.urls')),
    path('', include('Historico_Salarial.urls')),
]
