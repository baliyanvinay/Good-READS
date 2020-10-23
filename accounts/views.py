from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from accounts.forms import JoinForm


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'


class UserLogoutView(LogoutView):
    # Redirected directly to login page once logged out
    next_page = reverse_lazy('accounts:login')


class JoinView(FormView):
    template_name = 'accounts/signup.html'
    form_class = JoinForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        '''
        The function will validate form against the model(look for max_length, data type) and
        save it in the table.
        '''
        form.save()
        return super().form_valid(form)


class AuthorsView(TemplateView):
    template_name = 'accounts/authors.html'
