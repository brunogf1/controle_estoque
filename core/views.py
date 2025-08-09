from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, Produto, Almoxarifado, OrdemServico

# Create your views here.

### View para LOGIN ###
def login_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        
        try:
            usuario = Usuario.objects.get(nome = nome, senha=senha)
            
            request.session['usuario_id'] = usuario.id
            request.session['usuario_nome'] = usuario.nome
            request.session['usuario_email'] = usuario.email
            request.session['usuario_nivel'] = usuario.nivel_acesso

            return redirect ('menu')
        
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuário ou senha inválidos!')
    return render (request, 'login.html')

### View para o MENU ###
def menu_view(request):
    if not request.session.get('usuario_id'):
        return redirect ('login') 
    return render (request, 'menu.html')

def logou_view(request):
    request.session.flush()
    return redirect('login')

from .models import Almoxarifado, Produto

def visualizar_itens(request):
    if not request.session.get('usuario_id'):
        return redirect('login')

    # Filtragem
    codigo = request.GET.get('codigo') or ''
    descricao = request.GET.get('descricao') or ''
    um = request.GET.get('um') or ''
    almox_id = request.GET.get('almox_principal_id') or ''

    itens = Produto.objects.select_related('almox_principal_id').all()
    if codigo:
        itens = itens.filter(codigo__icontains=codigo)
    if descricao:
        itens = itens.filter(descricao__icontains=descricao)
    if um:
        itens = itens.filter(UM__icontains=um)
    if almox_id:
        itens = itens.filter(almox_principal_id=almox_id)

    almoxarifados = Almoxarifado.objects.all()
    return render(request, 'visualizar_itens.html', {'itens': itens, 'almoxarifados': almoxarifados})

def criar_ordem_servico(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        descricao = request.POST.get('descricao')
        OrdemServico.objects.create(codigo = codigo, descricao = descricao)
        
    return redirect('menu')