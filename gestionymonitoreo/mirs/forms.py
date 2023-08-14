from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
            'hora': forms.TimeInput(attrs={'placeholder': 'hh:mm:ss'}),
            # Otros campos y widgets...
        }