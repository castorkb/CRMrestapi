from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile  # Убедитесь, что импорт верный

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
        )

        # Создаем профиль для нового пользователя
        Profile.objects.create(user=user)  # Создайте профиль здесь

        # Попробуем добавить пользователя в группу "Клиенты"
        try:
            group = Group.objects.get(name="Клиенты")
            user.groups.add(group)
        except Group.DoesNotExist:
            raise serializers.ValidationError({"group": "Группы 'Клиенты' не существует."})

        user.save()
        return user















