from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from books.forms import BookForm


class IndexView(TemplateView):
    # Main index page view
    template_name = 'books/index.html'


class BookAddView(CreateView):
    template_name = 'books/add_book.html'
    form_class = BookForm
    success_url = reverse_lazy('books:index')
