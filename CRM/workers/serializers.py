from django.contrib.auth.models import User, Group
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    group = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'group']

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            )

        group_name = validated_data['group']

        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            raise serializers.ValidationError({"group": "This group does not exist."})

        user.groups.add(group)
        user.save()

        return user
