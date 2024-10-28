from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from .models import Project
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated


# Представление для регистрации
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
# Представление для получения JWT-токенов




################################################################
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Проверяем, что пользователь имеет право создать проект (например, только менеджеры)
        if not self.request.user.groups.filter(name='Менеджер').exists():
            raise PermissionDenied("У вас нет прав на создание проекта.")
        serializer.save()

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Проверяем права на редактирование проекта
        project = self.get_object()
        if project.manager != self.request.user:
            raise PermissionDenied("У вас нет прав на редактирование этого проекта.")
        serializer.save()

    def perform_destroy(self, instance):
        # Проверяем права на удаление проекта
        if instance.manager != self.request.user:
            raise PermissionDenied("У вас нет прав на удаление этого проекта.")
        instance.delete()