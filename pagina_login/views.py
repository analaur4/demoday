from django.shortcuts import render

# Create your views here.
def chamar_login(request):
    return render (request, 'login.html')

def chamar_notificacoes(request):
    return render(request, 'notificacoes.html')