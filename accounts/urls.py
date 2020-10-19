from django.urls import path
from . import views

from django.views.generic import RedirectView
# RedirectView will redirect url--> www.google.com/accounts/ to www.google.com/accounts/login/

urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=True)),
    path('login/', views.login, name='login'),
    path('join/', views.join, name='join'),
]
