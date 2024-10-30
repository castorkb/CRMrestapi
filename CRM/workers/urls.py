from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import RegisterView, AddTeamMemberView, RemoveTeamMemberView

from .views import ProjectListCreateView, ProjectDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='workers_register'),  # Регистрация
    path('api/token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),  # Логин (получение JWT)
    path('token/refresh/', TokenRefreshView.as_view(), name='workers_token_refresh'),  # Обновление JWT
    path('projects/', ProjectListCreateView.as_view(), name='project_list_create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/add_team_member/', AddTeamMemberView.as_view(), name='add_team_member'),
    path('projects/<int:pk>/remove_team_member/', RemoveTeamMemberView.as_view(), name='remove_team_member'),
]