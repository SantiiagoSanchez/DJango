from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def buscar(request):

    return render(request, "getproducto.html")

def getproduct(request):

    mensaje = 'Articulo buscado: %r' %request.GET["product"] #El get siempre en mayusculas, pq sino da error xd.

    return HttpResponse(mensaje)