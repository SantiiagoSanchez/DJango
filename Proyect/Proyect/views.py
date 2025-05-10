from django.http import HttpRequest, HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render


class Persona(object):
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):
    

    persona1 = Persona("Santiago", "Sanchez")

    nombre_completo = persona1.nombre + " " + persona1.apellido

    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    ahora = datetime.datetime.now()

    #doc_externo = open("C:/Users/Sanch/OneDrive/Escritorio/DJango/Proyect/Proyect/Plantillas/saludo.html")

    #plt = Template(doc_externo.read())

    #doc_externo.close()

    #doc_externo = loader.get_template('saludo.html')

    #context = Context({"Nombre": persona1.nombre, "Apellido": persona1.apellido, "Actual": ahora, "Temas": temas, "NombreCompleto": nombre_completo})

    #$documento = doc_externo.render({"Nombre": persona1.nombre, "Apellido": persona1.apellido, "Actual": ahora, "Temas": temas, "NombreCompleto": nombre_completo})

    return render(request, "saludo.html", {"Nombre": persona1.nombre, "Apellido": persona1.apellido, "Actual": ahora, "Temas": temas, "NombreCompleto": nombre_completo})

def cursoc(request):
    ahora = datetime.datetime.now()

    return render(request, "cursoc.html", {"Actual": ahora})

def cursocss(request):
    return render(request, "cursocss.html")

def despedida(request):

    doc_externo = loader.get_template('despedida.html')

    #plt = Template(doc_externo.read())

    #doc_externo.close()

    #context = Context()

    documento = doc_externo.render()

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