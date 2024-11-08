from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


# Create your models here.




class Inventory(models.Model):
    item_name = models.CharField(max_length=250)
    stock_Level = models.IntegerField()
    purchase_order = models.IntegerField()






class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()  # Поле для подробного описания проекта
    deadline = models.DateField(default=timezone.now)  # Дата завершения проекта
    status = models.CharField(max_length=250)  # Статус проекта (например, "В процессе", "Завершен")


    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_projects')
    team = models.ManyToManyField(User, related_name='team_projects', blank=True)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='client_projects')

    def __str__(self):
        return self.title


class Task(models.Model):
    task_name = models.CharField(max_length=250)   # Название задачи, до 250 символов
    title = models.CharField(max_length=250)  # Заголовок задачи, до 250 символов
    description = models.TextField()  # Полное описание задачи, поддерживает большой объем текста
    status = models.CharField(max_length=250)  # Статус задачи


    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='assigned_tasks'
        )  # Кто присвоен этой задаче

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='tasks'
        )  # К какому проекту принадлежит эта задача

    def __str__(self):  # Метод, возвращающий строковое представление задачи
        return self.task_name




class Resource(models.Model):
    name = models.CharField(max_length=250)  # Название ресурса ('Цемент', 'Бетон', и т. д.)
    type = models.CharField(max_length=250)  # Тип ресурса ('Строительный материал', 'Оборудование', и т. д.)
    quantity = models.CharField(max_length=250)  # Количество ресурса ( 100 кг, 50 штук и т. д.)
    availability = models.CharField(max_length=250)  # Доступность ресурса ('В наличии', 'Нет в наличии', и т. д.)
    usage_history = models.CharField(max_length=250)  # История использования ресурса ('Используется на проекте A', 'Использовался в проекте B' и т. д.)


class Financial(models.Model):
    budget = models.CharField(max_length=250)  # Бюджет проекта, сохраненный как текст
    expenses = models.CharField(max_length=250)  # Расходы, сохраненные как текст
    invoices = models.CharField(max_length=250)  # Счета-фактуры, сохраненные как текст
    payments = models.CharField(max_length=250)  # Платежи, сохраненные как текст
    taxes = models.CharField(max_length=250)  # Налоги, сохраненные как текст




















