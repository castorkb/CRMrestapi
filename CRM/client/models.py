from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=250)  # Имя клиента
    client_email = models.EmailField(max_length=250)  # Электронная почта клиента
    client_phonenamber = models.CharField(max_length=20)  # Номер телефона клиента

class Profile(models.Model):
    # Метод для строки, который возвращает имя клиента
    user = models.OneToOneField(User, on_delete=models.CASCADE)


from django.db import models
from django.contrib.auth.models import User  # Для связи с пользователем

class Interaction(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager_interactions')  # Менеджер
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_interactions')  # Клиент
    type = models.CharField(max_length=100)  # Тип взаимодействия (например, звонок, встреча и т.д.)
    date = models.DateTimeField(auto_now_add=True)  # Дата взаимодействия
    details = models.TextField()  # Описание взаимодействия

    def __str__(self):
        return f"Interaction with {self.client.username} by {self.manager.username} on {self.date}"

