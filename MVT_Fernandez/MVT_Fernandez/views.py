from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from proyectoMVT.models import *

def lista_personas(request):
       
    archivo = open(r"MVT_Fernandez\templates\lista_personas.html")
    
    plantilla = Template(archivo.read())

    archivo.close()

    listado_personas = Persona.objects.all()
  
    datos = {"listado_personas": listado_personas}

    contexto = Context(datos)
    
    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)