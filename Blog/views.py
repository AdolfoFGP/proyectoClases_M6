from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Publicacion
from .forms import TweetForm, ContactoForm, ComentarioForm
from django.contrib import messages
# vamos a traer vistas genericas para el tema CRUD
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

'''def home(request):
    return HttpResponse('<h1> hola chaval </h1>')

def contacto(request):
    return HttpResponse('<h1> Página de contactos </h1>')'''
# Create your views here.

'''publicaciones = [
    {
        'autor': 'Freddy',
        'titulo': 'Comer atuncito',
        'contenido': 'Me gusta el atuncito',
        'fecha': '13/07/23'
    },
    {
        'autor': 'Liz',
        'titulo': 'Comer pollito',
        'contenido': 'Me gusta el pollito',
        'fecha': '13/07/23'  
    },
    {
        'autor': 'Adolfo',
        'titulo': 'Comer papitas',
        'contenido': 'Me gustan las papitas',
        'fecha': '13/07/23'  
    }
]'''

'''def home(request):
    return render(request, 'Blog/index.html', context={'nombre':'BLOG'})'''

def home(request):
    x = 1
    x = 2
    contexto = {
        'publicacionesLlave': Publicacion.objects.all() # Antes publicaciones - # Publicacion.objects.raw('SELECT * FROM Blog_publicacion WHERE id = 1')
    }
    return render(request, 'Blog/index.html', context=contexto)

#def contacto(request):
#    return render(request, 'Blog/contacto.html', {'titulo':'awakelab'})

# Formularios

def createTweet(request):
    if request.method == "POST":
        formulario_post = TweetForm(request.POST)
        if formulario_post.is_valid():
            formulario_post.save() #se guardara en base datos
   
    formulario_get = TweetForm()
    return render(request, 'Blog/tweet_create.html', {'formulario':formulario_get})

# Modifico el def Contacto:

def contacto(request):
    if request.method == "POST":
        formulario = ContactoForm(request.POST) # aqui recibe los datos
        if formulario.is_valid():
            texto = formulario.cleaned_data['texto'] # como se definiio el form 
            check = formulario.cleaned_data['check'] # igual
            mensaje_alerta = f'Texto enviado: {texto}. Checkeo politicas: {check}'
            messages.success(request, mensaje_alerta)
            print(mensaje_alerta)

    formulario_c = ContactoForm()
    contexto = {
        'titulo': 'Contacto',
        'formulario': formulario_c
    }
    return render(request, 'Blog/contacto.html', contexto)

'''def crear_comentario(request, publicacion_id): #ese públicacion id lo vemos en migrations en 0003_comentario. El id, que es primary key.
    publicacion = Publicacion.objects.get(pk=publicacion_id)
    if request.method == "POST":
        formulario = ComentarioForm(request.POST) #vlidar metodo
        if formulario.is_valid(): #validar contenido
            comentario = formulario.save(commit=False) #save valida pa guardar datos, pero antes, que no lo haga.
            #comentario es variable q guarda esos datos. Antes hacemos que comentario.usuario sera igual al que está en sesion
            comentario.usuario = request.user
            #recibir id de publi como param para asociar comentari oa la publi, lo hacemos arriba en parametros de la funcion
            # Lo llamamamos publicacion_id
            comentario.publicacion = publicacion
            comentario.save()
    else:
        formulario = ComentarioForm() #comentario vacio
    return render(request, 'Blog/crear_comentario.html', {'formulario':formulario})'''

from django.http import JsonResponse

def crear_comentario(request, publicacion_id):
    publicacion = Publicacion.objects.get(pk=publicacion_id)

    if request.method == "POST":
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.usuario = request.user
            comentario.publicacion = publicacion
            comentario.save()

            nuevo_comentario = {
                'autor': comentario.usuario.username,
                'contenido': comentario.contenido,
                'fecha': comentario.fecha.strftime('%Y-%m-%d %H:%M:%S'),
            }

            return JsonResponse(nuevo_comentario)
    else:
        formulario = ComentarioForm()

    return render(request, 'Blog/crear_comentario.html', {'formulario': formulario, 'publicacion_id': publicacion.id})

# Vistas Genericas

class PublicacionDetailView(DetailView):
    model = Publicacion
   # template_name = 'Blog/publicacion_detail.html' #django busca la ruta <app-enestecasoblog>/<model-asociado>_<viewtype>.html
                        # por defecto sería blog/publicacion/detail, x el detailview
                        #Pero aca le decimos cual es.


class PublicacionCreate(CreateView):
    model = Publicacion
    fields = ['titulo', 'contenido']
    # Django buscara de la siguiente forma publicacion_create
    # o decirle especificamente a la vista que quiero con template_name

    # podemos usarla para actualizar. Con _form.

    # En el html como no tenemos context, se llama form.


    # vamos sobreescribir un metodo, antes haciamos is_valid
    def form_valid(self, form):
        # recibimos lso datos y debemos hacer asosciacion usuario con el campo usuario de mi publicacion
        form.instance.autor = self.request.user
        return super().form_valid(form)
    

# Actualizar-editar
# si no definimos template, buscara igual. Pero aca esta creado xq tanto para create y update
# vamos a decir que renderice modelo_form. Osea publicacion_form.html
# pero la definiremos explicitamente
class PublicacionUpdateView(UpdateView):
    model = Publicacion
    template_name = 'Blog/publicacion_form_actualizar.html'
    fields = ['titulo', 'contenido']
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


# Delete, no enviar dato ni formulario. Solo indicar que elemento queremos eliminar

class PublicacionDeleteView(DeleteView):
    model = Publicacion
    template_name = 'Blog/publicacion_confirm_delete.html'
    success_url = reverse_lazy('blog-home')
