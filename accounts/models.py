from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    '''
    User model in Django model contains username, first_name, last_name, email, password, groups,
    user_permissions, is_staff, is_active, is_superuser, last_login, date_joined
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_author = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='user_photos/')

    def __str__(self):
        return f"{self.user.last_name}, {self.user.first_name}"
