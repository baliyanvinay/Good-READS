from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from accounts.forms import JoinForm


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
