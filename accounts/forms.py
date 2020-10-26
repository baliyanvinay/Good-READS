from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account


class JoinForm(UserCreationForm):
    ''' password1 and password2 are created within UserCreationForm class, needed to override to 
    add placeholder for display. 
    Note that only password is saved in model and password1 and password2 are used for validation of
    password only.
    '''
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'placeholder': 'Enter Password'}),
        strip=False,
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'placeholder': 'Enter Password again'}),
        strip=False,
    )

    class Meta:
        model = Account
        fields = ['first_name', 'last_name',
                  'username', 'password1', 'password2', 'is_author', 'picture', ]
        exclude = []
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name', 'autofocus': 'autofocus'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter Username'}),
        }
