from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from webapp.models import Projeto, Tarefa
from django.views.generic import ListView, CreateView, UpdateView
from .forms import ProjetoForm, TarefaForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    return render(request, "login.html")

class ProjetoCreateView(LoginRequiredMixin, CreateView):
    template_name = "projeto_form.html"
    model = Projeto
    form_class = ProjetoForm
    success_url = reverse_lazy("projetos:cadastrar")

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)
    
class ProjetosListView(LoginRequiredMixin, ListView):
    template_name = "projeto_list.html"
    model = Projeto
    context_object_name = "projetos"
    
class TarefasCreateView(LoginRequiredMixin, CreateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'tarefa_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.projeto = get_object_or_404(
            Projeto,
            id=self.kwargs['id_projeto']
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.id_projeto = self.projeto
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'projetos:listar_tarefas',
            kwargs={'id_projeto': self.projeto.id}
        )

class TarefasListView(LoginRequiredMixin, ListView):
    model = Tarefa
    template_name = "tarefa_list.html"
    context_object_name = "tarefas"

    def get_queryset(self):
        self.projeto = get_object_or_404(
            Projeto,
            id=self.kwargs['id_projeto']
        )
        return Tarefa.objects.filter(id_projeto=self.projeto)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projeto'] = self.projeto
        return context

class TarefaUpdateView(LoginRequiredMixin,UpdateView):
    model = Tarefa
    fields = []  
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.concluida = not self.object.concluida
        self.object.save()
        return redirect(
            'projetos:listar_tarefas',self.object.id_projeto.id)