from django.urls import path
from . import views

app_name = 'produtos'  # Define o namespace

urlpatterns = [
    #path('', views.produtos_list, name='produtos_list'),
    path('', views.index, name='index'),
    path('produtos/', views.produtos, name='produtos'),
    path('contato/', views.contato, name='contato'),
]