from django.urls import path
from books.views import IndexView, BookAddView, MyBookView, BookUpdateView

app_name = 'books'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_book', BookAddView.as_view(), name='add_book'),
    path('my_books', MyBookView.as_view(), name='my_books'),
    path('my_books/<int:pk>/update', BookUpdateView.as_view(), name='update_book'),
]
