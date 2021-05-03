from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    

    def __str__(self):
        return self.username

