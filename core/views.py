from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

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