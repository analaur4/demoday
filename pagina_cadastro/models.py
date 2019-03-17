from django.db import models

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length = 120)
    # sobrenome = models.CharField(max_length = 120)
    # nascimento = models.DateField()
    email = models.CharField(max_length = 120)
    senha = models.CharField(max_length = 20)    
    telefone = models.CharField(max_length = 20)
    celular = models.CharField(max_length = 20)
    estado = models.CharField(max_length = 50)
    cidade = models.CharField(max_length = 120)
    bairro = models.CharField(max_length = 50)
    
    # desenvolvimento web
    javaScript = models.BooleanField(default=False)
    angular = models.BooleanField(default=False)
    react = models.BooleanField(default=False)
    css = models.BooleanField(default=False)
    php = models.BooleanField(default=False)
    nodeJS = models.BooleanField(default=False)
    html = models.BooleanField(default=False)
    django = models.BooleanField(default=False)
    python = models.BooleanField(default=False)
    bootstrap = models.BooleanField(default=False)

    # linguagem de programação
    java = models.BooleanField(default=False)
    cSharp = models.BooleanField(default=False)
    cMaisMais = models.BooleanField(default=False)
    c = models.BooleanField(default=False)
    algoritmos = models.BooleanField(default=False)

    # negocios
    financas = models.BooleanField(default=False)
    empreendedorismo = models.BooleanField(default=False)
    comunicacoes = models.BooleanField(default=False)
    administracao = models.BooleanField(default=False)

    # TI e Software
    certificacaoTI = models.BooleanField(default=False)
    redeSeguranca = models.BooleanField(default=False)
    hardware = models.BooleanField(default=False)
    sistemasOperacionais = models.BooleanField(default=False)

    # produtividade no escritorio
    microsoft = models.BooleanField(default=False)
    apple = models.BooleanField(default=False)
    google = models.BooleanField(default=False)
    sap = models.BooleanField(default=False)
    oracle = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.nome