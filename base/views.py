from django.shortcuts import redirect, render, get_object_or_404
from base.models import Noticia, Perfil, Categorias, Imagem
from base.forms import BarraDePesquisaForm, NoticiaForm, PerfilForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Noticia
from PIL import Image
from datetime import date
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.contrib.auth import logout

def home(request):
    ultimas_noticias = Noticia.objects.all()
    return render(request, 'home.html', {'ultimas_noticias': ultimas_noticias})

def pesquisar_noticias(request):
    results = []
    form = BarraDePesquisaForm(request.GET)
    
    if form.is_valid():
        keyword = form.cleaned_data['keyword']
        print(f"Keyword: {keyword}")
        results = Noticia.objects.filter(titulo__icontains=keyword)

    ultimas_noticias = Noticia.objects.all()
    print(f"Ultimas Noticias: {ultimas_noticias}")

    return render(request, 'resultados_pesquisa.html', {'ultimas_noticias': ultimas_noticias, 'form': form, 'results': results})

    

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('logar_usuario')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})

    
def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

def deslogar_usuario(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('logar_usuario')

@login_required      
def criar_noticia(request):
    categorias = Categorias.objects.all()  
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, categorias=categorias)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.user_id = request.user.id      
            noticia.save()
            
            # Adicione o seguinte loop para associar categorias selecionadas à notícia
            for categoria_id in request.POST.getlist('categorias'):
                categoria = Categorias.objects.get(pk=categoria_id)
                noticia.categorias.add(categoria)
            
            for f in request.FILES.getlist('imagens'):
                name = f'{date.today}-{noticia.id}.jpg'
                img = Image.open(f)
                img = img.convert('RGB')

                # Convertendo a imagem para bytes
                buffer = BytesIO()
                img.save(buffer, format="JPEG")

                # Criando o objeto InMemoryUploadedFile com os dados da imagem
                img_final = InMemoryUploadedFile(buffer, None, name, 'image/jpeg', buffer.tell(), None)
    
                # Salvar a imagem no campo imagem_noticia do modelo Noticia
                noticia.imagem_noticia.save(name, img_final)
                
            return redirect('home')   
    else:
        form = NoticiaForm(categorias=categorias)

    return render(request, 'criar_noticia.html', {'form': form, 'categorias': categorias})

@login_required
def minhas_postagens(request):
    postagens = Noticia.objects.filter(user = request.user)
    return render(request, 'minhas_postagens.html', {'postagens': postagens})



@login_required
def meu_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user, defaults={'nome': request.user.username})

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
        
    else:
        form = PerfilForm(instance=perfil)

    context = {'form': form}
    return render(request, 'meu_perfil.html', context)


@login_required
def excluir_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    if request.user.id == noticia.user.id:  
        noticia.delete()

        messages.success(request, 'Post excluído com sucesso.')
    else:
        messages.error(request, 'Você não tem permissão para excluir este post.')

    return redirect('home')
    
    
def detalhes_noticia(request, noticia_id):        
    noticia = get_object_or_404(Noticia, pk = noticia_id)    
    return render(request, 'detalhes_noticia.html', {'noticia': noticia})

