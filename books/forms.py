from django import forms
from books.models import Book
from accounts.models import Account
from django.forms import ModelForm


class BookForm(ModelForm):
    # authors = forms.ModelMultipleChoiceField(queryset = Account.objects.filter(is_author=True))
    authors = forms.ChoiceField(
        choices=[(author.id, author.get_full_name) for author in Account.objects.filter(is_author=True)])

    class Meta:
        model = Book
        fields = ('title', 'genre', 'authors', 'short_desc',
                  'description', 'ratings', 'cover_picture', 'copies', 'date_added')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title', 'autofocus': 'autofocus'}),
        }
