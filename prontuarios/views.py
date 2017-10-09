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


def home(request):
	return render(request, 'prontuarios/index.html')
