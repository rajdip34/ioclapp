from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class LoginData(models.Model):
    userId = models.CharField(max_length=100,unique=True)
    passW = models.CharField(max_length=100)
    message = models.CharField(max_length=500,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
