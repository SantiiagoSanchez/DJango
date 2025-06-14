from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
# Create your views here.

def buscar(request):

    return render(request, "getproducto.html")

def getproduct(request):

    if  request.GET["product"]:

        #mensaje = 'Articulo buscado: %r' %request.GET["product"] #El get siempre en mayusculas, pq sino da error xd.

        producto = request.GET["product"]

        articulo=Articulos.objects.filter(Nombre__icontains=producto) #Esto filtra por Nombre, campo que esta en la tabla Articulos
                                                                      #"[CAMPO DE LA TABLA]__icontains"

        return render(request, "getbynombre.html", {"Articulos": articulo, "Query": producto})
    
    else:
        
        mensaje = 'ERROR: Ingresa un producto valido'

        return HttpResponse(mensaje)