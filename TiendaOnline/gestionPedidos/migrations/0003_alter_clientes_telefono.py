# Generated by Django 5.2.1 on 2025-06-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_alter_clientes_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='Telefono',
            field=models.CharField(max_length=10, verbose_name='Numero de telefono'),
        ),
    ]
