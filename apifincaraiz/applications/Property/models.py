from django.db import models
from applications.Ubication.models import Cities
from applications.Category.models import Categories
import datetime

# Crea el modelo para la tabla tipos de propiedad.
class PropertiesTypes(models.Model):
    """
    Definición del modelo para la tabla tipos de propiedades.
    """
    # atributos de la tabla
    name = models.CharField('Tipo de Propiedad', max_length=50)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=datetime.datetime.now)

    # configuraciones para el admin
    class Meta:
        verbose_name = 'Tipo Propiedad'
        verbose_name_plural = 'Tipos de Propiedades'
        ordering = ['name',]
        unique_together = ('name',)

    def __str__(self):
        return f"{self.name}"


# Crea el modelo para la tabla propiedades.
class Properties(models.Model):
    """
    Definición del modelo para la tabla propiedades.
    """
    list_transac = [('Buy', 'Buy'), ('Rent', 'Rent')]

    # atributos de la tabla
    titulo = models.CharField('Titulo', max_length=100, blank=None)
    image = models.ImageField('Imagen', upload_to='images', height_field=None, width_field=None, max_length=None)
    price = models.IntegerField('Precio', blank=None)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    baths = models.IntegerField('No de Baños', blank=None)
    beds = models.IntegerField('No de Habitaciones', blank=None)
    sqrt = models.IntegerField('Mts2', blank=None)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    property_types = models.ForeignKey(PropertiesTypes, on_delete=models.CASCADE)
    transaction_type = models.CharField('Tipo de Transacción', max_length=10, choices=list_transac)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=datetime.datetime.now)

    # configuraciones para el admin
    class Meta:
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'
        ordering = ['titulo', 'price', 'city', 'sqrt', 'category']
        unique_together = ('titulo',)

    def __str__(self):
        return f"{self.titulo}"


# Crea el modelo para la tabla tipos de propiedad.
class Reviews(models.Model):
    """
    Definición del modelo para la tabla tipos de propiedades.
    """
    rating_list = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),]

    # atributos de la tabla
    feedbak = models.CharField('Comentarios', max_length=50)
    rating = models.IntegerField('Calificación', blank=None, choices=rating_list)
    avatar = models.ImageField('Avatar', upload_to='images', height_field=None, width_field=None, max_length=None)
    property_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=datetime.datetime.now)

    # configuraciones para el admin
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['rating',]

    def __str__(self):
        return f"{self.feedbak}"
