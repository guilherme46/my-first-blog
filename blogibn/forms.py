from django import forms

from .models import Publicacao

class PubForm(forms.ModelForm):

    class Meta:
        model = Publicacao
        fields = ('titulo', 'texto', 'autor')