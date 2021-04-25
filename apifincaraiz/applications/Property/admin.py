from django.contrib import admin
from .models import PropertiesTypes, Properties, Reviews

# Personaliza admin para tipos de propuedades.
class PropertiesTypesAdmin(admin.ModelAdmin):
    # indica que cosas mostrar cuando se listen los registros del modelo
    list_display = ('status', 'name', 'create_at')
    # indica los campos de busqueda
    search_fields = ('name',)


# personaliza admin para ciudades
class PropertiesAdmin(admin.ModelAdmin):
    # indica que cosas mostrar cuando se listen los registros del modelo
    list_display = (
                    'id',
                    'status', 
                    'titulo', 
                    'image',
                    'price',
                    'baths',
                    'beds',
                    'sqrt',
                    'city',
                    'category',
                    'create_at',
                    )

    # indica los campos de busqueda
    search_fields = ('titulo', 'price', 'category', 'city',)

    # agrega filtradores para buscar por estado
    list_filter = ('category',)


# Personaliza admin para tipos de propuedades.
class ReviewsAdmin(admin.ModelAdmin):
    # indica que cosas mostrar cuando se listen los registros del modelo
    list_display = ('property_id', 'feedbak', 'rating', 'avatar', 'create_at')
    # indica los campos de busqueda
    search_fields = ('feedbak',)


# Registra los modelos para gestion en admin
admin.site.register(PropertiesTypes, PropertiesTypesAdmin)
admin.site.register(Properties, PropertiesAdmin)
admin.site.register(Reviews, ReviewsAdmin)