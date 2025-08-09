from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('menu/', views.menu_view, name='menu'),
    path('itens/', views.visualizar_itens, name='visualizar_itens'),
    path('ordemServico', views.criar_ordem_servico, name='criar_ordem_servico'),
  #  path('movimentacao/', views.movimentacao_estoque, name='movimentacao_estoque'),
  #  path('logout/', views.logout, name='logout'),
]