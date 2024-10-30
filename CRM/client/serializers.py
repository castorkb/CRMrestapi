from django.contrib.auth.models import User, Group
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True) # Добавляем поле для номера телефона


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'email', 'password']

    def create(self, validated_data, phone_number=None):

        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            )
        # Если нужно, обработайте `phone_number` отдельно
        if phone_number:
            # Логика для обработки номера телефона, например, сохраним в другой модели
            pass

        try:
            group = Group.objects.get(name="Клиенты")
        except Group.DoesNotExist:
            raise serializers.ValidationError({"group": "Группы 'Клиенты' не существует."})

        user.groups.add(group)
        user.save()

        return user












