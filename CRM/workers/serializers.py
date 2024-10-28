from django.contrib.auth.models import User, Group
from rest_framework import serializers


from .models import Project
from .models import Project




class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # Поле для пароля пользователя
    group = serializers.CharField(write_only=True) # Поле для группы

    class Meta:
        model = User # Модель User, с которой работает сериализатор
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'group'] # Перечисление полей, которые будут использоваться в сериализаторе

    def create(self, validated_data):
        # Создание нового пользователя с привязкой к группе

        user = (User.objects.create_user(
            username=validated_data['username'], # Добавляем поле
            first_name=validated_data['first_name'], # Добавляем поле
            last_name=validated_data['last_name'], # Добавляем поле
            password=validated_data['password'], # Добавляем поле
            email=validated_data.get('email', ''), # Добавляем поле
            ))
        group_name = validated_data['group'] # Получение группы по имени
        try:
            group = Group.objects.get(name=group_name) # Проверка наличия группы. Если группы нет, выкидывает ошибку.

        except Group.DoesNotExist:
            raise serializers.ValidationError({"group": "Этой группы не существует."})

        user.groups.add(group)
        user.save()

        return user




################################################################
class ProjectSerializer(serializers.ModelSerializer):
    status = serializers.CharField(default='Ожидает начала') # Поле для статуса проекта. Значение по умолчанию - 'Ожидает начала'
    manager = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True) # Поле для связи с менеджером проекта. Оно является обязательным
    team = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, required=False) # Поле для связи с командой проекта, позволяющее выбрать несколько пользователей
    client = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True) # Поле для связи с клиентом проекта

    class Meta:
        model = Project  # Указывает, что сериализатор связан с моделью Project
        fields = ['id', 'title', 'description', 'deadline', 'status', 'manager', 'team', 'client'] # Перечисление полей, которые будут использоваться в сериализаторе



##################################################################

