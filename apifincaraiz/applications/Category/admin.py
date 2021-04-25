from django.contrib import admin
from .models import Categories

# personaliza admin para categorias
class CategoriesAdmin(admin.ModelAdmin):
    # indica que cosas mostrar cuando se listen los registros del modelo
    list_display = ('status', 'name', 'create_at',)
    # indica los campos de busqueda
    search_fields = ('name',)


# Registra los modelos para gestion en admin
admin.site.register(Categories, CategoriesAdmin)
