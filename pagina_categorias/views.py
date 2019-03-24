from django.shortcuts import render

# Create your views here.
def chamar_categorias(request):
    return render(request, 'categorias.html')