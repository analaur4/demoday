from django.shortcuts import render

# Create your views here.
def chamar_home(request):
    return render(request, 'index.html')

def chamar_notificacoes(request):
    return render(request, 'notificacoes.html')