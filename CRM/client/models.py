from django.db import models

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=250)
    client_email = models.EmailField(max_length=250)
    client_phonenamber = models.CharField(max_length=20)


