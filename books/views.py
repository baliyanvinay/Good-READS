from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from books.forms import BookForm
from books.models import Book

from django.views.generic.edit import FormMixin
class IndexView(ListView):
    # Main index page view
    template_name = 'books/index.html'
    model = Book
    ordering = ['-id']
    # Pagination
    paginate_by = 8

    def get(self, request):
        # Calling rent_book function to sort out calculation of renting book
        if(request.GET.get('book_Id')):
            rent_book(request.GET.get('book_Id'))
        return super().get(request)

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
    template_name = 'books/search_book.html'

    def get(self, request):
        if request.GET.get('book'):
            search_book = request.GET.get('book')
            search_data={
                'book_list': Book.objects.filter(title__contains=search_book),
            }
            return render(request, template_name='books/search_book.html', context=search_data)
        # when the page is loaded first time|TemplateView class to handle get request
        return super().get(request)


def rent_book(book_id):
    book=Book.objects.get(id=book_id)
    if book.copies>=1:
        book.copies-=1 # book is rented
    else:
        # what happens when book.copies goes to zero| Should not be available for rent. 
        # add a message that book can't be rented
        pass
    book.save()