from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil
# Vamos a definir campos extras para el user
# Queremos agregar correo

'''class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=False)
    #campo = forms.CharField(required=False) #Este campo es opcional

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']'''


# Se actualiza para registro usuarios

class RegistroUsuarioForm(UserCreationForm): 
    campos = (
        ('administrador','admin'),
        ('usuario comun', 'usuario_comun'),
        ('moderador', 'moderador')
    )
    email = forms.EmailField(required=False)
    tipo_usuario = forms.ChoiceField(choices=campos) # este asigna el grupo
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'tipo_usuario']

# Creamos formulario para actualizar usuario
class ActualizarUsuariosForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ActualizarPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['imagen']
