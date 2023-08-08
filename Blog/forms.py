from django import forms 
from .models import Tweet, Publicacion, Comentario

# Formulario asociado al modelo
class TweetForm(forms.ModelForm):
    cuerpo = forms.CharField(required = True,
                             widget = forms.widgets.Textarea(
                                 attrs={
                                     "placeholder": "Escribe tu tweet acá...",
                                     "class": "textarea is-success is-medium",
                                 }
                             ))

    class Meta: # Muestra los campos que mostrara el formulario
        model = Tweet
        fields = ['cuerpo']

# Formulario no ligado a un modelo
class ContactoForm(forms.Form):
    texto = forms.CharField(label = 'Contactanos')
    check = forms.BooleanField(label = 'Acepta las politicas', required = False)


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']