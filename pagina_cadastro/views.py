from django.shortcuts import render
from pagina_cadastro.forms import FormCadastro

# Create your views here.
def criar_cadastro_view(request):
    formulario = FormCadastro(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        formulario = FormCadastro()

    contexto = {
        'cadastro' : formulario
    }

    return render(request, 'cadastro.html', contexto)

def fazer_login(request):
    return render(request, 'login.html')
    