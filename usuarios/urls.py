from django.urls import path
from . import views

urlpatterns = [

    # Usuarios
    path('', views.usuarios, name='usuarios'),
    path('edit/<int:id>/', views.usuarios_edit, name='usuarios_edit'),
    path('delete/<int:id>/', views.usuarios_delete, name='usuarios_delete'),
    path('view/<int:id>/', views.usuario_detalhes, name='usuario_detalhes'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
