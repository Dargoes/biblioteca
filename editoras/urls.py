from django.urls import path
from . import views

urlpatterns = [
    path('', views.editoras, name='editoras'),
    path('add/', views.editoras_add, name='editoras_add'),
    path('edit/<int:id>/', views.editoras_edit, name='editoras_edit'),
    path('delete/<int:id>/', views.editoras_delete, name='editoras_delete'),
    path('view/<int:id>/', views.editora_detalhes, name='editora_detalhes'),
]
