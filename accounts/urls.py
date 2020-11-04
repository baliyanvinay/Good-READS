from django.urls import path
from accounts.views import JoinView, AuthorsView, UserLoginView, UserLogoutView, ProfileView, ProfileUpdateView

from django.views.generic import RedirectView
# RedirectView will redirect url--> www.google.com/accounts/ to www.google.com/accounts/login/

app_name = 'accounts'
urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=True)),
    path('join/', JoinView.as_view(), name='join'),
    path('authors/', AuthorsView.as_view(), name='authors'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/update/',
         ProfileUpdateView.as_view(), name='profile_update'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
