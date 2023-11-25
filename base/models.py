from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image as Im


class Cadastro(models.Model):
    username = models.CharField(max_length = 50)  
    email = models.EmailField(max_length = 50, unique=True) 
    senha = models.CharField(max_length = 50)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return f'{self.username} [{self.email}]' 

    '''class Meta:
        verbose_name = 'Usuário Cadastrado' 
        verbose_name_plural = 'Usuários Cadastrados' 
        ordering = ['-data']'''
    
    
class Categorias(models.Model):
    categorias = models.CharField(max_length=40,)
    
    def __str__(self):
        return self.categorias


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    categorias = models.ManyToManyField(Categorias)
    data = models.DateTimeField(auto_now_add = True)
    imagem_noticia = models.ImageField(upload_to='imagem_noticia', blank=True, null=True)
    
  
    def __str__(self):
        return self.titulo
    
  

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add = True)
    foto_perfil = models.ImageField(upload_to ='comments_pics/', blank = True, null = True)
    
    
    def __str__(self):
        return f'{self.nome} - {self.noticia.titulo}'
    
    
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    foto_perfil = models.ImageField(upload_to='profile_pics/', default='default_profile.jpg')

    def __str__(self):
        return f'{self.nome} Perfil'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created and not hasattr(instance, 'perfil'):
            Perfil.objects.create(user=instance, nome=instance.username)


class Imagem(models.Model):
    imagem = models.ImageField(upload_to='imagem_noticia')
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)



