from django.urls import path
from books.views import IndexView, BookAddView

app_name = 'books'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_book', BookAddView.as_view(), name='add_book'),
    path('my_books', BookAddView.as_view(), name='my_books'),
]
