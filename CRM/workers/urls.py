from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import (
    RegisterView, AddTeamMemberView, RemoveTeamMemberView,
    ProjectListCreateView, ProjectDetailView,
    TaskListCreateView, TaskDetailView, InventoryViewSet,
    ResourceListCreateView, ResourceDetailView,
    FinancialListCreateView, FinancialDetailView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='workers_register'),  # Регистрация нового работника
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Логин (получение JWT)
    path('token/refresh/', TokenRefreshView.as_view(), name='workers_token_refresh'),  # Обновление JWT
    path('projects/', ProjectListCreateView.as_view(), name='project_list_create'),  # Просмотр списка всех проектов и создание нового проекта
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),  # Просмотр деталей конкретного проекта по его идентификатору
    path('projects/<int:pk>/add_team_member/', AddTeamMemberView.as_view(), name='add_team_member'),  # Добавление участника в проект по идентификатору проекта
    path('projects/<int:pk>/remove_team_member/', RemoveTeamMemberView.as_view(), name='remove_team_member'),  # Удаление участника из проекта по идентификатору проекта
    path('tasks/', TaskListCreateView.as_view(), name='task_list_create'),  # Просмотр списка задач и создание задачи
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),  # Просмотр, обновление и удаление конкретной задачи по идентификатору
    path('inventory/', InventoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='inventory_list_create'),  # Список всех объектов и создание нового
    path('inventory/<int:pk>/', InventoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='inventory_detail'),  # Просмотр, обновление и удаление объекта по идентификатору
    path('resources/', ResourceListCreateView.as_view(), name='resource_list_create'),
    path('resources/<int:pk>/', ResourceDetailView.as_view(), name='resource_detail'),
    path('financial/', FinancialListCreateView.as_view(), name='financial_list_create'),  # Список и создание финансовых данных
    path('financial/<int:pk>/', FinancialDetailView.as_view(), name='financial_detail'),  # Детали, обновление и удаление конкретной финансовой записи
]
