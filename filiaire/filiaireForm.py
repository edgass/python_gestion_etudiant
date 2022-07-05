from django.forms import ModelForm

from filiaire.models import Filiaire


class FiliaireForm(ModelForm):
    class Meta:
        model = Filiaire
        fields = ['name']