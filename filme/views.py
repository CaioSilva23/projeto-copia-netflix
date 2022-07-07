from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.


# def homepage(request):
#     return render(request, "homepage.html")

# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)

# FUNCAO EXIBE TEMPLATE
class Homepage(TemplateView):
    template_name = "homepage.html"


# FUNCAO EXIBE UMA LISTA DE VIEW
class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme  # objet_list -> lista de item


class Detalhesfilmes(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme  # object - 1 filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacao += 1
        filme.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilmes, self).get_context_data(**kwargs)
        filmes_relacionados = self.model.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context
    #
    # def get_context_data(self, **kwargs):
    #     context = super(Detalhesfilmes, self).get_context_data(**kwargs)
    #     # filtrar tabela de filmes, cuja categoria = categoria do filme da pagina
    #     filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)
    #     context=["filmes_relacionados"] = filmes_relacionados
    #     return context


class PesquisaFilme(ListView):
    template_name = "pesquisa.html"
    model = Filme  # objet_list -> lista de item

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None
