from django.shortcuts import render, get_object_or_404
from .models import Artigo, MembroEquipe


def index(request):
    return render(request, 'restauranteapolo/index.html')

def blog(request):
    artigos = Artigo.objects.order_by('-data')
    return render(request, 'restauranteapolo/blog.html', {'artigos': artigos})

def artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    return render(request, 'restauranteapolo/artigo.html', {'artigo': artigo})

def sobre(request):
    equipe = MembroEquipe.objects.all()
    return render(request, 'restauranteapolo/sobre.html', {'equipe': equipe})