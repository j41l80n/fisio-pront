from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'cpf',]
    ordering = ['first_name']
    # actions = ['aprovar_minicurso', 'desaprovar_minicurso']

class ConsultaAdmin(admin.ModelAdmin):
     list_display = ['cpf',]
     ordering = ['cpf',]
    # actions = ['aprovar_minicurso', 'desaprovar_minicurso']

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Consulta, ConsultaAdmin)
