from django.db import models

class Video(models.Model):
    nombre = models.CharField(max_length=200)
    url = models.URLField()
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.nombre

class Delito(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Colonia(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class C2(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    colonias = models.ManyToManyField(Colonia)

    def __str__(self):
        return self.nombre

class Folio(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='folios')
    delito = models.ForeignKey(Delito, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    colonia = models.ForeignKey(Colonia, on_delete=models.CASCADE)
    fecha_evento = models.DateField()

    def __str__(self):
        return f"Folio {self.id} - Video: {self.video.nombre}"
