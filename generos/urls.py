from django.urls import path
from . import views

urlpatterns = [
    path('', views.generos, name='generos'),
    path('add/', views.generos_add, name='generos_add'),
    path('edit/<int:id>/', views.generos_edit, name='generos_edit'),
    path('delete/<int:id>/', views.generos_delete, name='generos_delete'),
    path('view/<int:id>/', views.genero_detalhes, name='genero_detalhes'),

]
