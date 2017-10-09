# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.shortcuts import get_object_or_404, render
from . import views #ponto (.) significa diretorio atual
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.home, name='home'),
]
