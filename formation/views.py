from django.shortcuts import render

# Create your views here.

def formation(request):
    return render(request, 'formation.html')
