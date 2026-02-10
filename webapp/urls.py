from django.urls import path
from .views import home
from webapp.views import ProjetosListView, ProjetoCreateView, TarefasCreateView, TarefasListView, TarefaUpdateView


app_name = 'projetos'

urlpatterns = [
    
    path('', home, name='home'),
    path('projetos/', ProjetosListView.as_view(), name='listar'),
    path('projetos/novo/', ProjetoCreateView.as_view(), name='cadastrar'),
    path('projetos/<int:id_projeto>/tarefas/', TarefasListView.as_view(), name='listar_tarefas'),
    path('projetos/<int:id_projeto>/tarefas/nova/', TarefasCreateView.as_view(), name='cadastrar_tarefa'),
    path('tarefas/<int:pk>/editar/', TarefaUpdateView.as_view(), name='alterar_tarefa'),
]

