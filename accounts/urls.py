from django.urls import path
from accounts.views import JoinView, AuthorsView
from django.contrib.auth.views import LoginView

from django.views.generic import RedirectView
# RedirectView will redirect url--> www.google.com/accounts/ to www.google.com/accounts/login/

app_name = 'accounts'
urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=True)),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('join/', JoinView.as_view(), name='join'),
    path('authors/', AuthorsView.as_view(), name='authors'),
]
