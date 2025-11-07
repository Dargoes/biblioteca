from django.urls import path
from . import views

urlpatterns = [
    path('', views.emprestimos, name='emprestimos'),
    path('add/', views.emprestimos_add, name='emprestimos_add'),
    path('edit/<int:id>/', views.emprestimos_edit, name='emprestimos_edit'),
    path('delete/<int:id>/', views.emprestimos_delete, name='emprestimos_delete'),
    path('view/<int:id>/', views.emprestimo_detalhes, name='emprestimos_detalhes'),

]
