from django.shortcuts import render

# O nome aqui TEM que ser 'home' porque é o que você chamou no urls.py
def home(request): 
    return render(request, 'index.html')