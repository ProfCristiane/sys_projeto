from django.contrib import admin

# Register your models here.
from .models import Projeto, Tarefa

admin.site.register(Projeto)
admin.site.register(Tarefa)