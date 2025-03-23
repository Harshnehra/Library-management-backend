from django.contrib.auth.models import AbstractUser
from django.db import models

class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    isAdmin = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



# Create your models here.
