# que se genbere automaticamente un perfil cuando usuario haga un registro
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Perfil

# Para manejar un signals tengo que modificar el apps.py

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance) #crea un perfil

# ahora metodo que guarde perfil
@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
    instance.perfil.save()