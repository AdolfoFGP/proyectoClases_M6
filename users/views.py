from django.shortcuts import render, redirect
# Aplicamos formulario que ya existe en django:
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistroUsuarioForm, ActualizarPerfilForm, ActualizarUsuariosForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.

'''def registro(request):
    if request.method == "POST":
        formulario_p = UserCreationForm(request.POST)
        if formulario_p.is_valid():
            username = formulario_p.cleaned_data["username"]
            messages.success(request, f'Cuenta creada de forma exitosa para el usuario {username}')
            formulario_p.save() # si se usa. xd
            return redirect('blog-home') # el nombre de la pag principal
            # formulario_p.save(), no save. Lo crea directamente
        else:
            messages.error(request, 'Hubo un error en el registro')
    formulario = UserCreationForm()
    return render(request, "users/registro.html", {'formulario':formulario})'''

'''def registro(request):
    if request.method == "POST":
        formulario_p = RegistroUsuarioForm(request.POST)
        if formulario_p.is_valid():
            username = formulario_p.cleaned_data["username"]
            messages.success(request, f'Cuenta creada de forma exitosa para el usuario {username}')
            formulario_p.save() # si se usa. xd
            return redirect('blog-home') # el nombre de la pag principal
            # formulario_p.save(), no save. Lo crea directamente
        else:
            messages.error(request, 'Hubo un error en el registro')
    formulario = RegistroUsuarioForm()
    return render(request, "users/registro.html", {'formulario':formulario})'''

# modificamos para lo del usuario
def registro(request):
    if request.method == "POST":
        formulario_p = RegistroUsuarioForm(request.POST)
        if formulario_p.is_valid():
            # traigo el usuario y el dato del choicefield
            usuario = formulario_p.save(commit=False) # no guardo para aplicar la logica antes
            # busco el grupo que el usuario eligio
            grupo_seleccionado = formulario_p.cleaned_data["tipo_usuario"]
            # condicionales para asignacion al grupo correcto
            if grupo_seleccionado == 'admin':
                grupo = Group.objects.get(name='admin')
            elif grupo_seleccionado == 'usuario_comun':
                grupo = Group.objects.get(name='usuario_comun')
            elif grupo_seleccionado == 'moderador':
                grupo = Group.objects.get(name='moderador')
            # Se guarda    
            usuario.save()
            # Se asigna al grupo que decidio
            usuario.groups.add(grupo)

            username = formulario_p.cleaned_data["username"]
            messages.success(request, f'Cuenta creada de forma exitosa para el usuario {username}')

            return redirect('blog-home') # el nombre de la pag principal
            # formulario_p.save(), no save. Lo crea directamente
        else:
            messages.error(request, 'Hubo un error en el registro')
    formulario = RegistroUsuarioForm()
    return render(request, "users/registro.html", {'formulario':formulario})



# el decorator solo puedo llamar a perfil si estoy en una sesion activa.
'''@login_required
def perfil(request):
    return render(request, 'users/perfil.html', {'user':request.user}) #Puede ser sin el context
'''

#modifico este para actualizar usuario perfil:
@login_required
def perfil(request):
    if request.method == 'POST':
        #los campos de usuario van a ser del usuario que esta en sesion
        formulario_usuario = ActualizarUsuariosForm(request.POST, instance=request.user) 
        formulario_perfil = ActualizarPerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if formulario_usuario.is_valid() and formulario_perfil.is_valid():
            formulario_usuario.save()
            formulario_perfil.save()
            return redirect('perfil')
    else:
        # GET
        formulario_usuario = ActualizarUsuariosForm(instance=request.user.perfil) # no si se debería ir el param en estos 2
        formulario_perfil = ActualizarPerfilForm(instance=request.user.perfil)
    contexto = {
        'formulario_usuario': formulario_usuario,
        'formulario_perfil': formulario_perfil
    }
    return render(request, 'users/perfil.html', contexto)