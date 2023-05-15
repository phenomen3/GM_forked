from django.contrib import admin
from .models import Video, Folio, Delito, Colonia, C2

class VideoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_publicacion')

admin.site.register(Video, VideoAdmin)
admin.site.register(Folio)
admin.site.register(Delito)
admin.site.register(Colonia)
admin.site.register(C2)
