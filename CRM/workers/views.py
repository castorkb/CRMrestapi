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
        project = self.get_object()
        if project.manager != self.request.user:
            raise PermissionDenied("У вас нет прав на редактирование этого проекта.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.manager != self.request.user:
            raise PermissionDenied("У вас нет прав на удаление этого проекта.")
        instance.delete()

    # Метод для добавления сотрудника в команду проекта
    def add_team_member(self, request, pk=None):
        project = self.get_object()
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            project.team.add(user)
            return Response({"status": "Сотрудник добавлен"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)

    # Метод для удаления сотрудника из команды проекта
    def remove_team_member(self, request, pk=None):
        project = self.get_object()
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            project.team.remove(user)
            return Response({"status": "Сотрудник удален"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)
class AddTeamMemberView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk=None):
        project = Project.objects.get(pk=pk)
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            project.team.add(user)
            return Response({"status": "Сотрудник добавлен"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)

class RemoveTeamMemberView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk=None):
        project = Project.objects.get(pk=pk)
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            project.team.remove(user)
            return Response({"status": "Сотрудник удален"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)