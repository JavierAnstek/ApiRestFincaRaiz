# Generated by Django 3.2 on 2021-04-24 06:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedbak', models.CharField(max_length=50, verbose_name='Comentarios')),
                ('rating', models.IntegerField(blank=None, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='Calificación')),
                ('avatar', models.ImageField(upload_to='images', verbose_name='Avatar')),
                ('create_at', models.DateTimeField(default=datetime.datetime.now)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property.properties')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'ordering': ['rating'],
            },
        ),
    ]
