from django.contrib import admin
from base.models import  Categorias, Noticia, Cadastro

# Register your models here.
@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'data']
    list_filter = ['data']

@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ['categoria']
    search_fields = ['categoria']
    list_filter = ['categoria']
    
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'user', 'data']
    search_fields = ['titulo', 'user']
    list_filter = ['data']
    
    
    
    

    
