from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from filiaire.filiaireForm import FiliaireForm
from filiaire.models import Filiaire


def createFiliaire(request):
    if request.method == "POST":
        name = request.POST.get("name")
        filiaire = FiliaireForm(request.POST)
        if filiaire.is_valid():
            filiaire.save()
            return redirect('home')
        else:
            context = {}
            messages.info(request, 'Veillez entrer une filiaire valide')
            return render(request, 'createFiliaire.html', context)

    return render(request, 'createFiliaire.html')

