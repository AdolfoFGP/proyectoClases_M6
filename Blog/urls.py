from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='blog-home'),
    path("contacto/", views.contacto, name='contacto-blog'),
    path("tweet/", views.createTweet, name='crear-tweet'),
    path('comentario/<int:publicacion_id>', views.crear_comentario, name='crear-comentario'),
    path('publicacion/<int:pk>', views.PublicacionDetailView.as_view(), name='publicacion-detalle'),
    path('publicacion/new', views.PublicacionCreate.as_view(), name='publicacion-crear'),
    path('publicacion/<int:pk>/update', views.PublicacionUpdateView.as_view(), name='publicacion-actualizar'),
    path('publicacion/<int:pk>/delete', views.PublicacionDeleteView.as_view(), name='publicacion-eliminar'),

]