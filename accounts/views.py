from django.contrib.auth import get_user_model, login, logout,authenticate
from django.shortcuts import render, redirect


# Create your views here.


def inscription(request):
    if request.method == "POST":
        name = request.POST.get("name")
        prenom = request.POST.get("prenom")
        birthday = request.POST.get("birthday")
        sexe = request.POST.get("sexe")
        niveau = request.POST.get("niveau")
        filiaire = request.POST.get("filiaire")
        tel = request.POST.get("tel")
        nationalite = request.POST.get("nationalite")

    return render(request, "inscription.html")


User = get_user_model()


def seConnecter(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
        return redirect('home')

    return render(request, "seConnecter.html")


def logout_user(request):
    logout(request)
    return redirect('front')


def createAccount(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'createAccount.html')
