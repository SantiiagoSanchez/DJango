from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto
# Create your views here.

def buscar(request):

    return render(request, "getproducto.html")

def getproduct(request):

    if  request.GET["product"]:

        #mensaje = 'Articulo buscado: %r' %request.GET["product"] #El get siempre en mayusculas, pq sino da error xd.

        producto = request.GET["product"]

        if len(producto) > 20:

            mensaje = 'ERROR: El texto es demasiado largo'

            return HttpResponse(mensaje)
        
        else:
            articulo=Articulos.objects.filter(Nombre__icontains=producto) #Esto filtra por Nombre, campo que esta en la tabla Articulos
                                                                          #"[CAMPO DE LA TABLA]__icontains"

            return render(request, "getbynombre.html", {"Articulos": articulo, "Query": producto})
    
    else:
        
        mensaje = 'ERROR: Ingresa un producto valido'

        return HttpResponse(mensaje)
    
def contacto(request):

    if request.method=="POST":
        
    #     Asunto = request.POST["asunto"]
    #     Mensaje = request.POST["mensaje"] + " " + request.POST["email"]
    #     Email_From = settings.EMAIL_HOST_USER 
    #     recipient_list = ["santiagosanchezz_21@hotmail.com"
    #     send_mail(Asunto, Mensaje, Email_From, recipient_list)
    #     return render(request, "gracias.html")
    # return render(request, "contacto.html")
        miformulario = FormularioContacto(request.POST)

        if miformulario.is_valid():

            data_form = miformulario.cleaned_data

            send_mail(data_form["asunto"], data_form["mensaje"], data_form.get("email", ""),["santiagosanchezz_21@hotmail.com"])

            return render(request, "gracias.html")
        
    else:

        miformulario = FormularioContacto()

    return render(request, "formulario_contacto.html", {"form": miformulario})

