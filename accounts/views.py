from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from accounts.forms import JoinForm
from accounts.models import Account


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'


class UserLogoutView(LogoutView):
    # Redirected directly to login page once logged out
    next_page = reverse_lazy('accounts:login')


class JoinView(FormView):
    template_name = 'accounts/signup.html'
    form_class = JoinForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        '''
        The function will validate form against the model(look for max_length, data type) and
        save it in the table.
        '''
        form.save()
        return super().form_valid(form)


class AuthorsView(ListView):
    model = Account
    template_name = 'accounts/authors.html'

    def get_queryset(self):
        # only getting the users where author flag is set to True
        return Account.objects.filter(is_author=True)


class ProfileView(DetailView):
    model = Account
    template_name = 'accounts/profile.html'
    '''
    DetailView will pick the pk from Url path and try to find the corresponding pk in model Account,
    Once found the object will be passed to template as 'object'
    '''
    # DetailView looks for pk or slug| Changed to look for username using get_object method

    def get_object(self):
        return Account.objects.get(username=self.kwargs.get("username"))


class ProfileUpdateView(UpdateView):
    template_name = 'accounts/signup.html'
    model = Account
    form_class = JoinForm

    # by default the updateview looks for pk or slug to get current_object| passing username to url dispather
    def get_object(self):
        return Account.objects.get(username=self.kwargs.get("username"))

    # get_success_url needs to be added to pass username as kwargs to url dispather
    def get_success_url(self):
        return reverse_lazy('accounts:profile', kwargs={'username': self.kwargs.get('username')})
