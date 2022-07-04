from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')
    return {"lista_filmes_recentes": lista_filmes}


def lista_filmes_alta(request):
    lista_alta = Filme.objects.all().order_by('-visualizacao')[0:10]
    return {'lista_filmes_alta': lista_alta}
