from django.urls import path
from accounts.views import JoinView, AuthorsView, UserLoginView

from django.views.generic import RedirectView
# RedirectView will redirect url--> www.google.com/accounts/ to www.google.com/accounts/login/

app_name = 'accounts'
urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=True)),
    path('login/', UserLoginView.as_view(), name='login'),
    path('join/', JoinView.as_view(), name='join'),
    path('authors/', AuthorsView.as_view(), name='authors'),
]
