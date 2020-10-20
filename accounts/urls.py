from django.urls import path
from accounts.views import LoginView, JoinView, AuthorsView

from django.views.generic import RedirectView
# RedirectView will redirect url--> www.google.com/accounts/ to www.google.com/accounts/login/

urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=True)),
    path('login/', LoginView.as_view(), name='login'),
    path('join/', JoinView.as_view(), name='join'),
    path('authors/', AuthorsView.as_view(), name='authors'),
]
