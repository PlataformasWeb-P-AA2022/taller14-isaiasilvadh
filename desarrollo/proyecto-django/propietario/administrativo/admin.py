from django.contrib import admin

from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import *


class PropietarioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'edad', 'nacionalidad')
    search_fields = ('nombre', 'apellido')

admin.site.register(Propietario, PropietarioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('costo_departamento', 'numero_cuartos', 'propietario')

    raw_id_fields = ('propietario',)

admin.site.register(Departamento, DepartamentoAdmin)
