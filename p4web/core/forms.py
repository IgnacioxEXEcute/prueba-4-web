from django import forms
from django.forms import ModelForm
from .models import Libro

class LibroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(LibroForm, self).__init__(*args, **kwargs)
        self.fields['ISBN'].required = False
        self.fields['nombreLibro'].required = False
        self.fields['autor'].required = False
        self.fields['Descripcion'].required = False
        self.fields['categoria'].required = False
    class Meta:
        model = Libro
        fields = ['ISBN','nombreLibro','autor','Descripcion','categoria',]