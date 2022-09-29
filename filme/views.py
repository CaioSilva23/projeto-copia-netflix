from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


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
class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme  # objet_list -> lista de item


class Detalhesfilmes(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme  # object - 1 filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacao += 1
        filme.save()
        # FILMES JÁ VISTOS PELO USUÁRIO
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilmes, self).get_context_data(**kwargs)
        filmes_relacionados = self.model.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context


class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme  # objet_list -> lista de item

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None
