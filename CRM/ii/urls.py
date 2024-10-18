from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='client_register'),  # Регистрация
    path('login/', CustomTokenObtainPairView.as_view(), name='client_login'),  # Логин (получение JWT)
    path('token/refresh/', TokenRefreshView.as_view(), name='client_token_refresh'),  # Обновление JWT
]
