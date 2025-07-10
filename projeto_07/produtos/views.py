from django.shortcuts import render

# Create your views here.

def produtos_list(request):
    return render(request, 'produtos/produtos_list.html')

def index(request):
    return render(request, 'produtos/index.html', {'title': 'Home'})

def produtos(request):
    return render(request, 'produtos/produtos.html', {'title': 'Produtos'})

def contato(request):
    return render(request, 'produtos/contato.html', {'title': 'Contato'})

