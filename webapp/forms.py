from django.forms import ModelForm
from .models import Projeto, Tarefa

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome','descricao']

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo','concluida']
        exclude = ['id_projeto', 'cadastrado_por']