from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Task(models.Model):
    TaskName = models.CharField(max_length=250)
    Title = models.CharField(max_length=250)
    Description = models.TextField
    Status = models.IntegerField
    Assigned_To = models.IntegerField

class Inventory(models.Model):
    ItemName = models.CharField(max_length=250)
    Stock_Level = models.IntegerField
    Purchase_Order = models.IntegerField




################################
class Project(models.Model):
    Title = models.CharField(max_length=250)
    Description = models.TextField()  # Добавлен вызов метода
    Deadline = models.DateField(default=timezone.now)
    Status = models.CharField(max_length=250)

    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_projects')
    team = models.ManyToManyField(User, related_name='team_projects', blank=True)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='client_projects')

    def __str__(self):
        return self.Title




################################




class Resource(models.Model):
    Name = models.CharField(max_length=250)
    Type = models.CharField(max_length=250)
    Quantity = models.CharField(max_length=250)
    Availability = models.CharField(max_length=250)
    Usage_History = models.CharField(max_length=250)


class Financial(models.Model):
    Budget = models.CharField(max_length=250)  # Бюджет проекта, сохраненный как текст
    Expenses = models.CharField(max_length=250) # Расходы, сохраненные как текст
    Invoices = models.CharField(max_length=250) # Счета-фактуры, сохраненные как текст
    Payments = models.CharField(max_length=250) # Платежи, сохраненные как текст
    Taxes = models.CharField(max_length=250) # Налоги, сохраненные как текст




















