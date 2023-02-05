from django.db import models

# Create your models here.

#creando una clase con el proyecto para crear el modelo

class Project(models.Model): #heredando de la clase MODELO de Django
    title=models.CharField(max_length=200,verbose_name="Titulo") #maneja texto simple (1 linea de texto)
    description=models.TextField(verbose_name="Descripción")  #maneja parrafos de texto
    image=models.ImageField(verbose_name="Imagen", upload_to="projects")
    #PAra asignar links (pueda que este en blanco o nulo, no siempre se tienen urls)
    link=models.URLField(null=True, blank=True,verbose_name="Enlace")
    
    #por auditoria se debe crear datos de creacion y actualizacion
    created=models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creacion") #sirve para guardar registro del tiempo y guarda automaticamente el modelo ( no cambia, es permanetne)
    updated=models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición") #Guarda automaticamente el cambio

    #uso de metadatos para modificar extendidas del modelo
    class Meta:
        verbose_name="proyecto"
        verbose_name_plural="proyectos"
        ordering=["-created"]
        #metodo para mostrar el nombre de los temas por el titulo (projectos)
       
    def __str__(self):
        return self.title