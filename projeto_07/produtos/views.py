from django.shortcuts import render

# Create your views here.

def produtos_list(request):
    return render(request, 'produtos/produtos_list.html')