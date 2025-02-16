from django.contrib import admin
from . models import Setor


class SetorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


admin.site.register(Setor, SetorAdmin)
