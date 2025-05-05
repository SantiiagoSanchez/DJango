from django.http import HttpRequest, HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):
    

    persona1 = Persona("Nicolas", "Sanchez")

    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    #nombre = "Santiago"

    #apellido = "Sanchez"

    ahora = datetime.datetime.now()

    doc_externo = open("C:/Users/Sanch/OneDrive/Escritorio/DJango/Proyect/Proyect/Plantillas/saludo.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    context = Context({"Nombre": persona1.nombre, "Apellido": persona1.apellido, "Actual": ahora, "Temas": temas})

    documento = plt.render(context)

    return HttpResponse(documento)

def despedida(request):

    doc_externo = open("C:/Users/Sanch/OneDrive/Escritorio/DJango/Proyect/Proyect/Plantillas/despedida.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    context = Context()

    documento = plt.render(context)

    return HttpResponse(documento)

    
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