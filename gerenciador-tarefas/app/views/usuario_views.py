from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required 


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def cadastro_usuarios_view(request):
    return render(request, 'cadastro_usuarios.html')

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('listar_tarefas')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {"form_usuario": form_usuario})


def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('dashboard')  # Redireciona para o dashboard após login
        else:
            messages.error(request, 'As credenciais de usuário estão incorretas')
            return redirect('logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html', {"form_login": form_login})


def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')

def cadastro_usuarios_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Cria um novo usuário
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        # Redireciona de volta para o dashboard após o cadastro
        return redirect('dashboard')
    
    return render(request, 'cadastro_usuarios.html')
