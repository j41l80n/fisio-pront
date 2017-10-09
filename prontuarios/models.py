# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse

from django.core.mail import send_mail
from django.utils.http import urlquote
from django.dispatch import receiver
from django.core import validators
from django.utils import timezone
from django.conf import settings
from django.db import models
import datetime #custom
from simple_history.models import HistoricalRecords #custom
from django.contrib.auth.views import password_reset, password_reset_confirm #custom
from django.core.urlresolvers import reverse_lazy #custom

class Paciente(User):
    username_validator = ASCIIUsernameValidator()
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    instituicao_ensino = models.CharField(('Instituição de ensino'), max_length=20, blank=False)
    idade = models.IntegerField(('Idade'))
    telefone = models.CharField(('Telefone'), max_length=20, blank=True)
    cpf = models.CharField(('CPF'), max_length=20, blank=True)
    history = HistoricalRecords()
    # objects = UserManager()

    def __str__ (self):
        return self.username

class Consulta(models.Model):
    telefone = models.CharField(('Telefone'), max_length=20, blank=True)
    cpf = models.CharField(('CPF'), max_length=20, blank=True)
    history = HistoricalRecords()
    paciente = models.ForeignKey("Paciente")
    def __str__ (self):
        return self.cpf
