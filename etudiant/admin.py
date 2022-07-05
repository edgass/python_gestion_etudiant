from django.contrib import admin

# Register your models here.
from etudiant.models import Etudiant, Filiaire, Niveau

admin.site.register([Etudiant, Filiaire, Niveau])
