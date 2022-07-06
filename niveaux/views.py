from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from niveaux.niveauForm import NiveauForm


def createNiveau(request):
    if request.method == "POST":
        name = request.POST.get("name")
        niveau = NiveauForm(request.POST)
        if niveau.is_valid():
            niveau.save()
            return redirect('home')
        else:
            context = {}
            messages.info(request, 'Veillez verifier les informations entrées')
            return render(request, 'createNiveau.html', context)

    return render(request, 'createNiveau.html')