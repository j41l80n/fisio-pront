# -*- coding: utf-8 -*-
from django.shortcuts import render #custom
from django.shortcuts import redirect, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import Group, Permission #custom
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout #custom
from django.conf import settings
from django.core.urlresolvers import reverse #custom
import datetime
# from .forms import * #custom
from .models import * #custom

def home(request):
	pacientes = Paciente.objects.all()
	return render(request, 'prontuarios/index.html', {'pacientes': pacientes})

def detalhes(request, id):
	consultas = Consulta.objects.filter(pk=id)
	# consnultas = Consnultas.objects.all()
	return render(request, 'prontuarios/detalhes.html', {'consultas': consultas})
