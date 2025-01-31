from django.contrib import admin
from .models import Cargo


class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


admin.site.register(Cargo, CargoAdmin)
