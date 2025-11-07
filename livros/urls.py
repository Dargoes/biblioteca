from django.urls import path
from . import views

urlpatterns = [

    path('', views.livros, name='livros'),
    path('add/', views.livros_add, name='livros_add'),
    path('edit/<int:id>/', views.livros_edit, name='livros_edit'),
    path('delete/<int:id>/', views.livros_delete, name='livros_delete'),
    path('view/<int:id>/', views.livro_detalhes, name='livro_detalhes'),

]
