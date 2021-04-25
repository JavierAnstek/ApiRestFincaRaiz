from django.db import models
import datetime

# Crea el modelo para la tabla Categorias.
class Categories(models.Model):
    """
    Definición del modelo para la tabla categorias.
    """
    # atributos de la tabla
    name = models.CharField('Categoria', max_length=50)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=datetime.datetime.now)

    # configuraciones para el admin
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name',]
        unique_together = ('name',)

    def __str__(self):
        return f"{self.name}"
