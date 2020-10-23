from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from accounts.forms import JoinForm


class LoginView(TemplateView):
    template_name = 'accounts/login.html'


class JoinView(FormView):
    template_name = 'accounts/signup.html'
    form_class = JoinForm


class AuthorsView(TemplateView):
    template_name = 'accounts/authors.html'
