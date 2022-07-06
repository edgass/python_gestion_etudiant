from django.forms import ModelForm

from niveaux.models import Niveau


class NiveauForm(ModelForm):
    class Meta:
        model = Niveau
        fields = ['name', 'mensualite']
