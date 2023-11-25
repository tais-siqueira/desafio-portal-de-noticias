from django.contrib import admin

from base.models import  Categorias, Noticia, Comentario, Cadastro
# Register your models here.
@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'data']
    search_fields = ['username', 'email']
    list_filter = ['data']

@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ['categorias']
    search_fields = ['categorias']
    list_filter = ['categorias']
    
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'user', 'data']
    search_fields = ['titulo', 'user']
    list_filter = ['data']
    
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['texto', 'data']
    search_fields = ['texto', 'data']
    
    
    

    
