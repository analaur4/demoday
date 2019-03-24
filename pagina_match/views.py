from django.shortcuts import render

# Create your views here.
def chamar_confirmar_match(request):
    return render(request, 'confirmar-match.html')

def chamar_procurar(request):
    return render(request, 'procurar.html')

def chamar_procurar_dw(request):
    return render(request, 'procurar=dw.html')