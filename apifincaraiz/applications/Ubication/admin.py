from django.contrib import admin
from .models import States, Cities

# Personaliza admin para estados.
class StateAdmin(admin.ModelAdmin):
    # indica que cosas mostrar cuando se listen los registros del modelo
    list_display = ('status', 'name', 'create_at')
    # indica los campos de busqueda
    search_fields = ('name',)
    

# personaliza admin para ciudades
class CitiesAdmin(admin.ModelAdmin):
    # indica que cosas mostrar cuando se listen los registros del modelo
    list_display = ('status', 'name', 'zip_code', 'state', 'create_at',)
    # indica los campos de busqueda
    search_fields = ('name', 'zip_code',)

    # agrega filtradores para buscar por estado
    list_filter = ('state',)


# Registra los modelos para gestion en admin
admin.site.register(States, StateAdmin)
admin.site.register(Cities, CitiesAdmin)