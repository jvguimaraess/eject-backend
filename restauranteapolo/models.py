from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='autores/', blank=True)

    def __str__(self):
        return self.nome
    
class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data = models.DateField()
    imagem = models.ImageField(upload_to='artigos/', blank=True)
    legenda_imagem = models.CharField(max_length=200, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
class MembroEquipe(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='equipe/', blank=True)

    def __str__(self):
        return f"{self.nome} - {self.cargo}"
    
class Destaque(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    icone = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
    
class Servico(models.Model):
    nome = models.CharField(max_length=200)
    icone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome