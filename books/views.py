from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from books.forms import BookForm
from books.models import Book


class IndexView(ListView):
    # Main index page view
    template_name = 'books/index.html'
    model = Book
    ordering = ['-id']
    # Pagination
    paginate_by = 8


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
        queryset = Book.objects.filter(author=self.request.user)
        return queryset

    def get(self, request, *agrs, **kwargs):
        '''
        Get to check if queryset is empty- 
        Yes: Redirect to add_book url 
        No: Display my_books
        '''
        self.object_list = self.get_queryset()
        if not self.object_list:
            # Redirect to add_book when querySet is empty| Meaning when no data
            return redirect('books:add_book')
        context = self.get_context_data()
        return self.render_to_response(context)


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/add_book.html'
    form_class = BookForm
    success_url = reverse_lazy('books:my_books')


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('books:my_books')

    # Get request method is changed to use post directly skipping the _confirm_delete template
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class SearchView(TemplateView):
    template_name='books/search_book.html'