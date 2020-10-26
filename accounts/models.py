from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Account(AbstractUser):
    '''
    User model in Django model contains username, first_name, last_name, email, password, groups,
    user_permissions, is_staff, is_active, is_superuser, last_login, date_joined
    '''
    is_author = models.BooleanField(default=False)
    picture = models.ImageField(
        upload_to='user_photos/', default='accounts/images/default-profile.png')

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
