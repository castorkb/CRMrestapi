from django.db import models

# Create your models here.
class Client(models.Model):
    clientName = models.CharField(max_length=250)
    clientEmail = models.EmailField(max_length=250)
    clientPhonenamber = models.CharField(max_length=20)


