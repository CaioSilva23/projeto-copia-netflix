# url - view - template

from django.urls import path, include
from .views import Homepage, Homefilmes, Detalhesfilmes, PesquisaFilme
from django.contrib.auth import views as auth_view

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilmes.as_view(), name='detalhesfilme'),
    path('pesquisa/', PesquisaFilme.as_view(), name='pesquisa'),
    path('login/', auth_view.LoginView.as_view(templates_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(templates_name='logout.html'), name='logout')
]
