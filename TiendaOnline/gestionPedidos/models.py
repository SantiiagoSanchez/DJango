from django.db import models

class Clientes(models.Model):
    Nombre = models.CharField(max_length=30) #CharField es para decir que es texto lo que se va a guardar
    Direccion = models.CharField(max_length=50)
    Email = models.EmailField(blank=True, null=True) #Esto es para decirle que no es requerido, que puede ser null
    Telefono = models.CharField(max_length=10, verbose_name="Numero de telefono") #verbose_name es para que en el panel de administracion salga el label con ese nombre

    def __str__(self):
        return self.Nombre
    
    
class Articulos(models.Model):
    Nombre = models.CharField(max_length=30)
    Categoria = models.CharField(max_length=30)
    Precio = models.IntegerField() #Campo de tipo entero

    def __str__(self):
        return "Nombre: %s - Categoria: %s - Precio: $%s" % (self.Nombre, self.Categoria, self.Precio)

class Pedidos(models.Model):
    Numero = models.IntegerField()
    Fecha = models.DateField() #Campo para fechas como un datetime.
    Entregado = models.BooleanField() #Campo booleano