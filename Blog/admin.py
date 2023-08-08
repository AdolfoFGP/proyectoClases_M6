from django.contrib import admin
from .models import Publicacion, Tweet, Comentario

# Register your models here.

admin.site.register(Publicacion)
admin.site.register(Tweet)
admin.site.register(Comentario)