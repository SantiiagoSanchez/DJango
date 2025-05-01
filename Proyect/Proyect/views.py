from django.http import HttpRequest, HttpResponse

def saludo(request):
    
    return HttpResponse("Hola mundo, primer pagina con DJango.")

def despedida(request):

    return HttpResponse("Nos vemos, Despedida en DJango.")