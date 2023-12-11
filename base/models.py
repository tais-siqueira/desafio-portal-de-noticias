from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image as Im


class Cadastro(AbstractUser):
    email = models.EmailField(max_length = 50, unique=True)
    data = models.DateTimeField(auto_now_add = True)
    password = models.CharField(max_length=128, default='some_default_value')
    
    class Meta:
        swappable = 'AUTH_USER_MODEL'
    
    def __str__(self): 
        return f'{self.username} [{self.email}]' 

    
    
class Categorias(models.Model):
    categoria = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.categoria


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    categorias = models.ManyToManyField(Categorias)
    data = models.DateTimeField(auto_now_add = True)
    imagem_noticia = models.ImageField(upload_to='imagem_noticia', blank=True, null=True)
    
  
    def __str__(self):
        return self.titulo
    
    
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



