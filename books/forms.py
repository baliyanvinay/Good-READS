from books.models import Book
from django.forms import ModelForm


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['date_added', 'copies']
