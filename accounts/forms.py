from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account


class JoinForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name',
                  'username', 'password1', 'password2', 'is_author', 'picture', ]
        exclude = []
        widgets = {
            'first_name': forms.fields.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'last_name': forms.fields.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            'username': forms.fields.TextInput(attrs={'placeholder': 'Enter Username'}),
            'password1': forms.fields.TextInput(attrs={'placeholder': 'Enter Username'}),
        }
