from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from .models import Interaction
from .serializers import InteractionSerializer
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):  # Представление для регистрации
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class CustomTokenObtainPairView(TokenObtainPairView):  # Представление для получения JWT-токенов
    permission_classes = (AllowAny,)








from rest_framework import generics
from .models import Interaction
from .serializers import InteractionSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Interaction
from .serializers import InteractionSerializer

class InteractionListCreateView(generics.ListCreateAPIView):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Фильтруем взаимодействия по текущему пользователю, как менеджеру
        return Interaction.objects.filter(manager=self.request.user)

    def perform_create(self, serializer):
        # При создании взаимодействия назначаем текущего пользователя как менеджера
        serializer.save(manager=self.request.user)


class InteractionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Interaction.objects.filter(client__user=self.request.user)
