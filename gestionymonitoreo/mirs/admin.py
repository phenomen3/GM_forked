from django.contrib import admin
from .models import Medio, Canal, Estacion, ProgramaRadio, ProgramaTV, RedSocial, Tema, Subtema, Tipo, Submotivo, Subtipo, Mencion, Noticia


# registro de los modelos de 
admin.site.register(Medio)
admin.site.register(Canal)
admin.site.register(Estacion)
admin.site.register(ProgramaRadio)
admin.site.register(ProgramaTV)
admin.site.register(RedSocial)
admin.site.register(Tema)
admin.site.register(Subtema)
admin.site.register(Tipo)
admin.site.register(Submotivo)
admin.site.register(Subtipo)
admin.site.register(Mencion)
admin.site.register(Noticia)
