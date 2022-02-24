from re import template
from sre_constants import SUCCESS
from django.views.generic import CreateView

from django.urls import reverse_lazy

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


class LogIn(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('post:index')
    template_name = 'users/login.html'


class LogOut(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('post:index')
    template_name = 'users/logout.html'