"""gestionEtudiant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.views import logout_user, seConnecter, createAccount
from etudiant.views import home, listEtudiants, singleEtudiant, inscriptionEtudiant, updateEtudiant, deleteEtudiant
from filiaire.views import createFiliaire
from front.views import front
from gestionEtudiant import settings

urlpatterns = [
    path('', front, name='front'),
    path('signin/', seConnecter, name='signin'),
    path('createAccount/', createAccount, name='createAccount'),
    path('updateEtudiant/<int:pk>', updateEtudiant, name='updateEtudiant'),
    path('deleteEtudiant/<int:pk>', deleteEtudiant, name='deleteEtudiant'),
    path('inscription/', inscriptionEtudiant, name='inscription'),
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home'),
    path('listEtudiants/', listEtudiants, name='listEtudiants'),
    path('etudiant/<int:slug>/', singleEtudiant, name="etudiant"),
    path('createFiliaire/', createFiliaire, name="createFiliaire"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
