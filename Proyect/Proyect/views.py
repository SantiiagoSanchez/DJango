from django.http import HttpRequest, HttpResponse
import datetime

def saludo(request):
    
    return HttpResponse("Hola mundo, primer pagina con DJango.")

def despedida(request):

    return HttpResponse("Nos vemos, Despedida en DJango.")

    
def fechactual(response):

    fecha = datetime.datetime.now()

    documento = """
    <html>
    <body>
    <h1 style="color: #48e">
    Fecha y hora actual %s
    </h1>
    </body>
    </html>    
    """ %fecha

    return HttpResponse(documento)

def edadporparametro(request, edad, anio):
    
    periodo = anio - 2025
    edad_futura = edad + periodo
    documento = ("<html><body><h1>En el año %s tendras %s años" %(anio, edad_futura))

    return HttpResponse(documento)