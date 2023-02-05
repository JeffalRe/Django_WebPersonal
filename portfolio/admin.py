from django.contrib import admin
#se importa la libreria proyecto
from .models import Project
# Register your models here.
#crear clase para agregar configuracion en el administrador configuracion extendida
class ProjectAdmin(admin.ModelAdmin):
    #sirve para ver datos creados en el modelo portfolio
    readonly_fields=('created','updated')
    
#Registrar el modelo de administrador
admin.site.register(Project,ProjectAdmin)



