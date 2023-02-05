#Se debe importar el HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
#crear html

#portada para el html // crear vista 
#vista envia peticion
def home(request):
    #llamar al template html
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def contact(request):
    return render(request,"core/contact.html")    
