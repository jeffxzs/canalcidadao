from django.shortcuts import render

# Create your views here.

def inicial(request):
    return render(request, 'index.html')

def areas(request):
    return render(request, 'areas.html')

def area_cadastro(request):
    return render(request, 'area_cadastro.html')

