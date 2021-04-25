from django.db import models
import datetime

# Crea el modelo para la tabla Estados.
class States(models.Model):
    """
    Definición del modelo para la tabla state.
    """
    # atributos de la tabla
    name = models.CharField('Estado', max_length=50)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=datetime.datetime.now)

    # configuraciones para el admin
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['name',]
        unique_together = ('name',)

    def __str__(self):
        return f"{self.name}"


# Crea el modelo para la tabla Ciudades.
class Cities(models.Model):
    """
    Definición del modelo para la tabla ciudades.
    """
    # atributos de la tabla
    name = models.CharField('Ciudad', max_length=50)
    zip_code = models.CharField('Código Zip', max_length=50)
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=datetime.datetime.now)

    # configuraciones para el admin
    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['name', 'state',]
        unique_together = ('name', 'state')

    def __str__(self):
        return f"{self.name}"