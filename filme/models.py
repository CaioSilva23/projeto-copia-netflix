from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models heradsadasaaaa

LISTA_CATEGORIAS = (
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)


# criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100, default='Titulo')
    thumb = models.ImageField(upload_to='thumb_filmes', default='')
    descrica = models.TextField(max_length=1000, default='')
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS, default='')
    visualizacao = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo


# criar espisodios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, default='Titulo')
    video = models.URLField(default='')

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField('Filme')
