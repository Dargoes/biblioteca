from django.urls import path
from . import views

urlpatterns = [
    path('', views.autores, name='autores'),
    path('add/', views.autores_add, name='autores_add'),
    path('edit/<int:id>/', views.autores_edit, name='autores_edit'),
    path('delete/<int:id>/', views.autores_delete, name='autores_delete'),
    path('view/<int:id>/', views.autor_detalhes, name='autor_detalhes'),
]
