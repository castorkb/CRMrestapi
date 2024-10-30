from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Task(models.Model):
    taskname = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField
    status = models.IntegerField
    assigned_To = models.IntegerField

class Inventory(models.Model):
    itemName = models.CharField(max_length=250)
    stock_Level = models.IntegerField
    purchase_Order = models.IntegerField




################################
class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()  # Добавлен вызов метода
    deadline = models.DateField(default=timezone.now)
    status = models.CharField(max_length=250)

    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_projects')
    team = models.ManyToManyField(User, related_name='team_projects', blank=True)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='client_projects')

    def __str__(self):
        return self.title




################################




class Resource(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    quantity = models.CharField(max_length=250)
    availability = models.CharField(max_length=250)
    usage_history = models.CharField(max_length=250)


class Financial(models.Model):
    budget = models.CharField(max_length=250)  # Бюджет проекта, сохраненный как текст
    expenses = models.CharField(max_length=250) # Расходы, сохраненные как текст
    invoices = models.CharField(max_length=250) # Счета-фактуры, сохраненные как текст
    payments = models.CharField(max_length=250) # Платежи, сохраненные как текст
    taxes = models.CharField(max_length=250) # Налоги, сохраненные как текст




















