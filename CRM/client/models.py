from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=250)
    client_email = models.EmailField(max_length=250)
    client_phonenamber = models.CharField(max_length=20)




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
