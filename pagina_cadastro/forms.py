from django import forms
from pagina_cadastro.models import Cadastro

class FormCadastro(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = [
            'nome',
            'email',
            'senha',
            'telefone',
            'celular',
            'estado',
            'cidade',
            'javaScript',
            'angular',
            'react',
            'css',
            'php',
            'nodeJS',
            'html',
            'django',
            'python',
            'bootstrap',
            'java',
            'c',
            'algoritmos',
            'financas',
            'empreendedorismo',
            'comunicacoes',
            'administracao',
            'certificacaoTI',
            'redeSeguranca',
            'hardware',
            'sistemasOperacionais',
            'microsoft',
            'apple',
            'google',
            'sap',
            'oracle',
        ]
        widgets = { #serve para especificar um campo 
            'senha' : forms.PasswordInput(),

        }