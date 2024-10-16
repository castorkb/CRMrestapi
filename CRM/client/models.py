from django.db import models

# Create your models here.
class Client(models.Model):
    ClientName = models.CharField(max_length=250)
    ClientEmail = models.EmailField(max_length=250)
    ClientPhonenamber = models.CharField(max_length=20)


