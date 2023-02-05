from django.shortcuts import render

#importar modelo para ingresar la informacion en web (vista)
from .models import Project


# Create your views here.

def portfolio(request):
    #obtener la lista de proyectos almacenados en admi
    projects=Project.objects.all()
    
    return render(request,"portfolio/portafolio.html",{'projects':projects})


