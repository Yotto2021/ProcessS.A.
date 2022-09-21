from django.contrib import admin
from .models import Contrato, Rol, Unidad_Interna, Usuarios, Flujo, Tarea, Responsable_Flujo, Responsable_Tarea

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["nombre_full", "rut", "username", "password", "fec_nac", "genero", "Contrato", "Rol", "Unidad_Interna"]
    list_editable = ["username", "password", "Contrato", "Rol", "Unidad_Interna"]
    search_fields = ["nombre_full"]
    list_filter = ["Contrato"]
    #list_per_page = 10

admin.site.register(Contrato)
admin.site.register(Rol)
admin.site.register(Unidad_Interna)
admin.site.register(Usuarios, UsuarioAdmin)
admin.site.register(Flujo)
admin.site.register(Tarea)
admin.site.register(Responsable_Flujo)
admin.site.register(Responsable_Tarea)