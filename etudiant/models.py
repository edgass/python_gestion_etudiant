from django.db import models
import secrets

# Create your models here.
from django import forms

from filiaire.models import Filiaire
from gestionEtudiant import settings
from niveaux.models import Niveau








class Etudiant(models.Model):
    name = models.CharField(max_length=128)
    prenom = models.CharField(max_length=128)
    birthday = models.DateField()
    sexe = models.CharField(max_length=128)
    nationalite = models.CharField(max_length=128)
    matricule = models.CharField(max_length=128, default=secrets.token_hex(5))
    photo = models.ImageField(upload_to="etudiantProfil")
    ref_filiaire = models.ForeignKey(Filiaire, on_delete=models.CASCADE)
    ref_niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=128)

    def __str__(self):
        return self.prenom

