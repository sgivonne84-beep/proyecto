from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Aviso, Noticia, Colaborador

class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Usuario', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#agregado

class AvisoForm(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = ('titulo', 'descripcion')

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'descripcion', 'fotografia')

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ('nombre', 'descripcion', 'fotografia')


