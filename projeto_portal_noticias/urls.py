"""
URL configuration for projeto_portal_noticias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static 
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from base.views import home, detalhes_noticia, cadastrar_usuario, criar_noticia, minhas_postagens, meu_perfil, logar_usuario, excluir_noticia, deslogar_usuario, pesquisar_noticias



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', home, name='home'),
    path('cadastrar_usuario/', cadastrar_usuario, name="cadastrar_usuario"),
    path('logar_usuario/', logar_usuario, name="logar_usuario"),
    path('logout/', deslogar_usuario, name='deslogar_usuario'),
    path('noticia_detalhe/<int:noticia_id>/', detalhes_noticia, name='noticia_detalhe'),
    path('criar_postagem/', criar_noticia, name='criar_noticia'),
    path('minhas_postagens/', minhas_postagens, name='minhas_postagens'),
    path('meu_perfil/', meu_perfil, name='meu_perfil'),
    path('excluir_noticia/<int:noticia_id>/', excluir_noticia, name='excluir_noticia'),
    path('resultados_pesquisa/', pesquisar_noticias, name='resultados_pesquisa')

    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
