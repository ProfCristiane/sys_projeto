from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(default='')
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    titulo = models.CharField(max_length=150)
    concluida = models.BooleanField(default=False)
    id_projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.titulo