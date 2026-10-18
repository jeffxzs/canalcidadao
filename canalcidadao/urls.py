from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.inicial, name='inicial'),

    path('categorias/', views.categoria_lista, name='categoria_lista'),
    path('categorias/cadastro/', views.categoria_cadastro, name='categoria_cadastro'),
    path('categorias/<int:pk>/editar/', views.categoria_editar, name='categoria_editar'),
    path('categorias/<int:pk>/remover/', views.categoria_remover, name='categoria_remover'),

    path('bairros/', views.bairro_lista, name='bairro_lista'),
    path('bairros/cadastro/', views.bairro_cadastro, name='bairro_cadastro'),
    path('bairros/<int:pk>/editar/', views.bairro_editar, name='bairro_editar'),
    path('bairros/<int:pk>/remover/', views.bairro_remover, name='bairro_remover'),

    path('usuarios/', views.usuario_lista, name='usuario_lista'),
    path('usuarios/cadastro/', views.usuario_cadastro, name='usuario_cadastro'),
    path('usuarios/<int:pk>/editar/', views.usuario_editar, name='usuario_editar'),
    path('usuarios/<int:pk>/remover/', views.usuario_remover, name='usuario_remover'),
]