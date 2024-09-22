from django.db import models
from django.contrib.auth.models import User


class registrar_usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    email = models.CharField(max_length=50)
    is_staff = models.BooleanField


class registrar_granja(models.Model):
    id_granja = models.AutoField(primary_key=True)
    nombre_granja = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    email = models.CharField(max_length=50)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class registrar_galpon(models.Model):
    id_galpon = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class registrar_encargado(models.Model):
    id_encargado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    email = models.CharField(max_length=50, default="activisionactivision7.@gmail.com")
    id_galpon = models.ForeignKey(registrar_galpon, on_delete=models.CASCADE)

class configurar_parametros(models.Model):
    id_config = models.AutoField(primary_key=True)
    tipo_aves = models.CharField(max_length=50)
    tem_minima = models.IntegerField()
    tem_maxima = models.IntegerField()
    hume_minima = models.IntegerField()
    hume_maxima = models.IntegerField()
    promedio_temperatura = models.IntegerField(default=25)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class mediciones(models.Model):
    id_medicion = models.AutoField(primary_key=True)
    temperatura = models.CharField(max_length=50)
    humedad = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    promedio_temperatura = models.IntegerField(default=25)
    id_config_parametro = models.ForeignKey(configurar_parametros, on_delete=models.CASCADE)

class Alerta(models.Model):
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    id_encargado = models.ForeignKey(registrar_encargado, on_delete=models.CASCADE)
    leida = models.BooleanField(default=False)
