from django.urls import path
from books.views import IndexView, BookAddView, MyBookView, BookUpdateView, BookDeleteView
from books.views import SearchView, BookRentView

app_name = 'books'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('add_book', BookAddView.as_view(), name='add_book'),
    path('my_books', MyBookView.as_view(), name='my_books'),
    path('my_books/<int:pk>/update', BookUpdateView.as_view(), name='update_book'),
    path('my_books/<int:pk>/delete', BookDeleteView.as_view(), name='delete_book'),
    path('rent/<int:pk>', BookRentView.as_view(), name='rent_book'),
]
