from django import forms
from .models import Video, Folio

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['nombre', 'url', 'fecha_publicacion']

class FolioForm(forms.ModelForm):
    class Meta:
        model = Folio
        fields = ['delito', 'direccion', 'colonia', 'fecha_evento']
