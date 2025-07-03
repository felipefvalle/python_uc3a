from django.urls import path
from . import views

app_name = 'produtos'  # Define o namespace

urlpatterns = [
    path('', views.produtos_list, name='produtos_list'),  
]