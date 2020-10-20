from django.shortcuts import render
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'accounts/login.html'


class JoinView(TemplateView):
    template_name = 'accounts/signup.html'
