from django.contrib import admin
from . models import Pessoa


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'rg', 'cpf', 'ctps', 'data_nascimento', 'genero')
    search_fields = ('nome', 'rg', 'cpf', 'ctps', 'data_nascimento', 'genero')


admin.site.register(Pessoa, PessoaAdmin)
