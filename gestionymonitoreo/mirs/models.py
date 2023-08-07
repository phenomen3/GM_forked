from django.db import models

class Medio(models.Model):
    nombre = models.CharField(max_length=100)

class Canal(models.Model):
    nombre = models.CharField(max_length=100)

class Estacion(models.Model):
    nombre = models.CharField(max_length=100)

class ProgramaRadio(models.Model):
    nombre = models.CharField(max_length=100)

class ProgramaTV(models.Model):
    nombre = models.CharField(max_length=100)

class RedSocial(models.Model):
    nombre = models.CharField(max_length=100)

class Tema(models.Model):
    nombre = models.CharField(max_length=100)

class Subtema(models.Model):
    nombre = models.CharField(max_length=100)

class Tipo(models.Model):
    nombre = models.CharField(max_length=100)

class Submotivo(models.Model):
    nombre = models.CharField(max_length=100)

class Subtipo(models.Model):
    nombre = models.CharField(max_length=100)

class Mencion(models.Model):
    palabra_clave = models.CharField(max_length=100)

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    hora = models.TimeField()
    polaridad = models.CharField(max_length=10)
    calificacion = models.PositiveIntegerField()
    autor_usuario = models.CharField(max_length=100)
    tema = models.ForeignKey(Tema, on_delete=models.DO_NOTHING)
    subtema = models.ForeignKey(Subtema, on_delete=models.DO_NOTHING)
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING)
    submotivo = models.ForeignKey(Submotivo, on_delete=models.DO_NOTHING)
    subtipo = models.ForeignKey(Subtipo, on_delete=models.DO_NOTHING)
    mencion = models.ForeignKey(Mencion, on_delete=models.DO_NOTHING)
    noticia_principal = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    medio = models.ForeignKey(Medio, on_delete=models.DO_NOTHING)
    canal = models.ForeignKey(Canal, on_delete=models.DO_NOTHING, null=True, blank=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.DO_NOTHING, null=True, blank=True)
    programa_radio = models.ForeignKey(ProgramaRadio, on_delete=models.DO_NOTHING, null=True, blank=True)
    programa_tv = models.ForeignKey(ProgramaTV, on_delete=models.DO_NOTHING, null=True, blank=True)
    red_social = models.ForeignKey(RedSocial, on_delete=models.DO_NOTHING, null=True, blank=True)
