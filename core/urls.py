from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('menu/', views.menu_view, name='menu'),
    
  #  path('itens/', views.visualizar_itens, name='itens'),
  #  path('movimentacao/', views.movimentacao_estoque, name='movimentacao_estoque'),
  #  path('logout/', views.logout, name='logout'),
]