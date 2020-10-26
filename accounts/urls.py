from django.urls import path
from accounts.views import JoinView, AuthorsView, UserLoginView, UserLogoutView, ProfileView

from django.views.generic import RedirectView
# RedirectView will redirect url--> www.google.com/accounts/ to www.google.com/accounts/login/

app_name = 'accounts'
urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=True)),
    path('join/', JoinView.as_view(), name='join'),
    path('authors/', AuthorsView.as_view(), name='authors'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
