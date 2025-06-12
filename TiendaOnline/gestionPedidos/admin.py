from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("Nombre","Direccion","Telefono")  #Esto es para que se vea en la lista como una nueva seccion.
    search_fields=("Nombre", "Telefono") #Esto es para habilitar una caja de busqueda por nombre o por telefono.

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos)
admin.site.register(Pedidos)
