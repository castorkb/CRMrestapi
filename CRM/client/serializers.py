from django.contrib.auth.models import User, Group
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:

        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'], # Добавляем поле
            first_name=validated_data['first_name'],  # Добавляем поле
            last_name=validated_data['last_name'],  # Добавляем поле
            password=validated_data['password'], # Добавляем поле
            email=validated_data.get('email', ''), # Добавляем поле
            )

        try:
            group = Group.objects.get(name="Клиенты")
        except Group.DoesNotExist:
            raise serializers.ValidationError({"group": "Группы 'Клиенты' не существует."})

        user.groups.add(group)
        user.save()

        return user












