from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    # Main index page view
    template_name = 'books/index.html'
