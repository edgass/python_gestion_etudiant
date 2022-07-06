
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime

# Create your views here.
from accounts.views import seConnecter
from etudiant.addEtudiantForm import EtudiantForm
from django.contrib import messages

from etudiant.models import Etudiant
from filiaire.models import Filiaire
from niveaux.models import Niveau


@login_required(login_url=seConnecter)
def home(request):
    nbrEtudiants = Etudiant.objects.all().count()
    nbrGarcons = Etudiant.objects.filter(sexe="Masculin").count()
    nbrFille = Etudiant.objects.filter(sexe="Feminin").count()
    nbrFiliaires = Filiaire.objects.all().count()
    return render(request, "home.html",
                  context={"nbrEtudiants": nbrEtudiants, "nbrGarcon": nbrGarcons, "nbrFille": nbrFille,
                           "nbrFiliaire": nbrFiliaires})


def listEtudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, "listEtudiants.html", context={"etudiants": etudiants})


def singleEtudiant(request, slug):
    etudiant = get_object_or_404(Etudiant, id=slug)
    return render(request, "singleEtudiant.html", context={"etudiant": etudiant})

def singleEtudiantForEtudiant(request, slug):
    etudiant = get_object_or_404(Etudiant, id=slug)
    return render(request, "singleEtudiantForEtudiant.html", context={"etudiant": etudiant})


def inscriptionEtudiant(request):
    niveau = Niveau.objects.all()
    filiaire = Filiaire.objects.all()
    if request.method == "POST":
        form = EtudiantForm(request.POST, request.FILES)
        print("printing post : ", request.POST)
        if form.is_valid():
            etd = form.save()
            etudiant = get_object_or_404(Etudiant, id=etd.id)
            return render(request, "singleEtudiantForEtudiant.html", context={"etudiant": etudiant})

    else:
            if request.POST.get('prenom') == '':
                messages.info(request, 'Le champ prénom ne doit pas etre vide')
            else:
                if request.POST.get('name') == '':
                    messages.info(request, 'Le champ nom ne doit pas etre vide')
                else:
                    if request.POST.get('birthday') == '':
                        messages.info(request, 'Entrez votre date de naissance')

    return render(request, "inscription.html", context={"niveaux": niveau, "filiaires": filiaire})

def updateEtudiant(request,pk):
    currentEtudiant = Etudiant.objects.get(id=pk)
    niveaux = Niveau.objects.all()
    filiaires = Filiaire.objects.all()
    if request.method == "POST":
        Etudiant.objects.filter(pk=pk).update(name=request.POST.get('name'), prenom=request.POST.get('prenom'), birthday=datetime.now(), ref_niveau=request.POST.get('ref_niveau'), ref_filiaire=request.POST.get('ref_filiaire'))
        return redirect('/home')

    return render(request, "updateEtudiant.html", context={"niveaux": niveaux, "filiaires": filiaires, "currentEtudiant": currentEtudiant})



def deleteEtudiant(request,pk):
    currentEtudiant = Etudiant.objects.get(id=pk)
    if request.method == "POST":
        currentEtudiant.delete()
        return redirect('listEtudiants')
