from django.contrib import admin
from .models import Genero


class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


admin.site.register(Genero, GeneroAdmin)
