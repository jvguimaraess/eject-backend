from django.db import models


class Artigo(models.Model):
    
    #Campos
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    conteudo = models.TextField()
    data = models.DateTimeField()
    legenda = models.CharField(max_length=200, blank=True)
    
    # Representação em string do modelo
    def __str__(self):
        return f"{self.titulo} por {self.autor} em {self.data.strftime('%Y-%m-%d %H:%M')}"

class Funcionario(models.Model):
    
    #Campos
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='funcionarios/')
    
    # Representação em string do modelo
    def __str__(self):
        return f"{self.nome} - {self.cargo}"

class destaque(models.Model):
    
    #Campos
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    icone = models.ImageField(upload_to='destaques/')
    
    # Representação em string do modelo
    def __str__(self):
        return self.titulo