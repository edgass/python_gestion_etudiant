from django.forms import ModelForm
from .models import Etudiant


class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = ['name', 'prenom', 'birthday', 'sexe', 'nationalite', 'ref_filiaire', 'ref_niveau', 'photo']
