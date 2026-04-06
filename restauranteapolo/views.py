from django.shortcuts import render

def index(request):
    return render(request, 'restauranteapolo/index.html')

def blog(request):
    return render(request, 'restauranteapolo/blog.html')

def artigo(request):
    return render(request, 'restauranteapolo/artigo.html')

def sobre(request):
    return render(request, 'restauranteapolo/sobre.html')