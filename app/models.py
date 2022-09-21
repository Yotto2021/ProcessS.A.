from pyexpat import model
from django.db import models

# Create your models here.
class Contrato(models.Model):
    contrato = models.CharField(max_length=32)
    fec_ini = models.DateField()
    fec_ter = models.DateField()

    def __str__(self):
        return self.contrato

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=32)

    def __str__(self):
        return self.nombre_rol

class Unidad_Interna(models.Model):
    nombre_unidad = models.CharField(max_length=32)

    def __str__(self):
        return self.nombre_unidad

opciones_contrato = [
    ["A Plazo"],
    ["Fijo"]
]

opciones_rol = [
    ["Administrador"],
    ["Funcionario"],
    ["Diseñador"]
]

opciones_unidad = [
    ["Gestión de Personas"],
    ["Logistica"],
    ["Contabilidad"],
    ["QA"],
    ["Calidad"]
]

class Usuarios (models.Model):
    nombre_full = models.CharField(max_length=70)
    rut = models.CharField(max_length=12)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    fec_nac = models.DateField()
    genero = models.CharField(max_length=16)
    Contrato = models.ForeignKey(Contrato, on_delete=models.PROTECT)
    Rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    Unidad_Interna = models.ForeignKey(Unidad_Interna, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_full

class Flujo(models.Model):
    descripcion = models.CharField(max_length=256)
    fec_creacion = models.DateField()
    fec_ini = models.DateField()
    fec_ter = models.DateField()
    estado = models.CharField(max_length=32)

    def __str__(self):
        return self.estado

class Tarea(models.Model):
    descripcion = models.CharField(max_length=256)
    prioridad = models.IntegerField()
    categoria = models.CharField(max_length=32)
    fec_creacion = models.DateField()
    fec_ini = models.DateField()
    fec_ter = models.DateField()
    estado = models.CharField(max_length=32)

    def __str__(self):
        return self.categoria

class Responsable_Flujo(models.Model):
    fk_usr = models.IntegerField()
    fk_tarea = models.IntegerField()
    Flujo = models.ForeignKey(Flujo, on_delete=models.PROTECT)
    Usuarios = models.ForeignKey(Usuarios, on_delete=models.PROTECT)

class Responsable_Tarea(models.Model):
    fk_usr = models.IntegerField()
    fk_tarea = models.IntegerField()
    Tarea = models.ForeignKey(Tarea, on_delete=models.PROTECT)
    Usuarios = models.ForeignKey(Usuarios, on_delete=models.PROTECT)