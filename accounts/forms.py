from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account


class JoinForm(UserCreationForm):
    class Meta:
        model = Account
        fields = '__all__'
        exclude = ['last_login', 'groups', 'is_active', 'email',
                   'is_staff', 'user_permissions', 'date_joined', 'is_superuser', 'password']
        widgets = {
            'first_name': forms.fields.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'last_name': forms.fields.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            'username': forms.fields.TextInput(attrs={'placeholder': 'Enter Username'}),
        }
