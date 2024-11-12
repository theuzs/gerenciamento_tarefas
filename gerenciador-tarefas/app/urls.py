from django.urls import path
from .views.tarefa_views import (
    listar_tarefas, cadastrar_tarefa, editar_tarefa, remover_tarefa
)
from .views.usuario_views import (
    cadastrar_usuario, logar_usuario, deslogar_usuario, dashboard_view
)

urlpatterns = [
    path('dashboard/', usuario_views.dashboard_view, name='dashboard'),
    path('cadastro-usuarios/', usuario_views.cadastro_usuarios_view, name='cadastro_usuarios'),
    path('', logar_usuario, name='logar_usuario'),  # Página de login
    path('dashboard/', dashboard_view, name='dashboard'),  # Página do dashboard
    path('tarefas/', listar_tarefas, name='listar_tarefas'),  # Lista de tarefas
    path('tarefas/cadastrar/', cadastrar_tarefa, name="cadastrar_tarefa"),  # Cadastro de tarefa
    path('tarefas/editar/<int:id>/', editar_tarefa, name="editar_tarefa"),  # Edição de tarefa
    path('tarefas/remover/<int:id>/', remover_tarefa, name="remover_tarefa"),  # Remoção de tarefa
    path('usuarios/cadastrar/', cadastrar_usuario, name="cadastrar_usuario"),  # Cadastro de usuário
    path('usuarios/logout/', deslogar_usuario, name="deslogar_usuario"),  # Logout do usuário
]