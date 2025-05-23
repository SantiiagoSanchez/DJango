from django.db import models

class Clientes(models.Model):
    Nombre = models.CharField(max_length=30) #CharField es para decir que es texto lo que se va a guardar
    Direccion = models.CharField(max_length=50)
    Email = models.EmailField()
    Telefono = models.CharField(max_length=10)

class Articulos(models.Model):
    Nombre = models.CharField(max_length=30)
    Categoria = models.CharField(max_length=30)
    Precio = models.IntegerField() #Campo de tipo entero

class Pedidos(models.Model):
    Numero = models.IntegerField()
    Fecha = models.DateField() #Campo para fechas como un datetime.
    Entregado = models.BooleanField() #Campo booleano