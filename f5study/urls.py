"""f5study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pagina_cadastro.views import criar_cadastro_view
from pagina_sobre.views import chamar_sobre
from pagina_home.views import chamar_home, chamar_notificacoes
from pagina_categorias.views import chamar_categorias
from pagina_match.views import chamar_confirmar_match, chamar_procurar, chamar_procurar_dw
from pagina_login.views import chamar_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', criar_cadastro_view, name='cadastro'),
    path('sobre/', chamar_sobre, name='sobre'),
    path('home/', chamar_home, name='home'),
    path('categorias/', chamar_categorias, name='categorias'),
    path('match/', chamar_confirmar_match, name='match'),
    path('procurar/', chamar_procurar, name='procurar'),
    path('procurar-dw/', chamar_procurar_dw, name='procurar-dw'),
    path('login/', chamar_login, name='login'),
    path('notificacoes/', chamar_notificacoes, name='notificacoes'),
]
