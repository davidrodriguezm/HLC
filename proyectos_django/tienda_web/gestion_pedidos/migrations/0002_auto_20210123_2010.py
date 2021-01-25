# Generated by Django 3.1.5 on 2021-01-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='articulos',
            name='precio',
            field=models.FloatField(verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='articulos',
            name='tipo',
            field=models.CharField(max_length=20, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(max_length=15, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='entregado',
            field=models.BooleanField(verbose_name='Entregado'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='fecha',
            field=models.DateField(verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='numero',
            field=models.IntegerField(verbose_name='Número'),
        ),
    ]
