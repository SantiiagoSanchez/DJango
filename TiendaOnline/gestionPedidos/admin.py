from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("Nombre","Direccion","Telefono")  #Esto es para que se vea en la lista como una nueva seccion.
    search_fields=("Nombre", "Telefono") #Esto es para habilitar una caja de busqueda por nombre o por telefono.

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("Categoria",) #Lista a la derecha para filtrar

class PedidosAdmin(admin.ModelAdmin):
    list_display=("Numero", "Fecha")
    list_filter=("Fecha",)
    date_hierarchy="Fecha" #Otro tipo de filtro.

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
