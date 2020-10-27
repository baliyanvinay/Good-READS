from django import forms
from books.models import Book
from django.forms import ModelForm


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'genre', 'author', 'short_desc',
                  'description', 'ratings', 'cover_picture', 'copies', 'date_added')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title', 'autofocus': 'autofocus'}),
        }
