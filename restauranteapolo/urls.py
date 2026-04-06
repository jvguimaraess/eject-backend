from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('artigo/', views.artigo, name='artigo'),
    path('sobre/', views.sobre, name='sobre'),
]