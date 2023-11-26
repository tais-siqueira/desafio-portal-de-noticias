from django.contrib.auth.forms import AuthenticationForm
from django import forms
from base.models import Cadastro, Noticia, Comentario, Perfil, Categorias, Imagem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget



class CadastroForm(UserCreationForm):
    class Meta:
        model = Cadastro
        fields = ['username', 'email', 'password1', 'password2']

    def clean_senha(self):
        senha = self.cleaned_data.get('password1')
        if not senha:
            raise forms.ValidationError('Este campo é obrigatório.')
        return senha
     
class LoginForm(forms.Form):
    '''username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)'''

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        
class CKEditorImageWidget(forms.ClearableFileInput):
    template_name = 'ckeditor/widgets/clearable_file_input.html'

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'categorias', 'conteudo', 'imagem_noticia']
        widgets = {
            'categorias': forms.CheckboxSelectMultiple(),
            'conteudo': CKEditorWidget(),
        }
    
    def __init__(self, *args, **kwargs):
        categorias = kwargs.pop('categorias', None)
        super(NoticiaForm, self).__init__(*args, **kwargs)
        if categorias:
            self.fields['categorias'].queryset = categorias


class ComentarioForm(forms.Form):
    class Meta:
        model = Comentario
        fields = ['texto', 'foto_perfil']


class BarraDePesquisaForm(forms.Form):
    keyword = forms.CharField(max_length=100, label='Palavra-chave')
    

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto_perfil']
        

    
