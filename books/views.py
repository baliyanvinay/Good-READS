from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from books.forms import BookForm
from books.models import Book


class IndexView(TemplateView):
    # Main index page view
    template_name = 'books/index.html'


class BookAddView(CreateView):
    template_name = 'books/add_book.html'
    form_class = BookForm
    success_url = reverse_lazy('books:index')


class MyBookView(ListView):
    model = Book
    template_name = 'books/my_books.html'
    '''
    Filters out the books for the current logged user
    '''

    def get_queryset(self):
        queryset = Book.objects.filter(author=1)
        return queryset
