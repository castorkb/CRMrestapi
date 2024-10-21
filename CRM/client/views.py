from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Представление для регистрации
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# Представление для получения JWT-токенов
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)




# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import RegistrationSerializer
#
# class RegisterView(APIView):
#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.data)  # Получаем данные из запроса
#         if serializer.is_valid():  # Проверяем, валидны ли данные
#             serializer.save()  # Сохраняем пользователя и добавляем в группу
#             return Response({"message": "Регистрация прошла успешно"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Ошибки валидации
#
#
# class CustomTokenObtainPairView:
#     pass