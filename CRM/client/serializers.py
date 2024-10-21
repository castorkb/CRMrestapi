from django.contrib.auth.models import User, Group
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            )

        try:
            group = Group.objects.get(name="Клиенты")
        except Group.DoesNotExist:
            raise serializers.ValidationError({"group": "The 'Клиенты' group does not exist."})

        user.groups.add(group)
        user.save()

        return user












