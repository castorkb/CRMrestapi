from django.db import models

# Create your models here.
class User(models.Model):
    UserName = models.CharField(max_length=250)
    UserEmail = models.EmailField(max_length=250)
    UserPassword = models.CharField(max_length=150)
    UserPhone = models.CharField(max_length=20)
    UserRole = models.CharField(max_length=100)

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

class Project(models.Model):
    Title = models.CharField(max_length=250)
    Description = models.TextField
    Deadline = models.TextField
    Status = models.CharField(max_length=250)

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




















