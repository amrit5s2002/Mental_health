from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    
class Counselor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    is_counselor = models.BooleanField(default=True)
    is_user = models.BooleanField(default=False)

class User_normal(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    is_counselor = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    
   