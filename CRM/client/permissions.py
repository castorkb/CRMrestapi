from rest_framework.permissions import BasePermission

class IsEmployee(BasePermission):
    # класс разрешений, который проверяет, состоит ли пользователь в группе
    def has_permission(self, request, view):
        return request.user.groups.filter(name='employee').exists()

class IsClient(BasePermission):
    # проверяет, состоит ли пользователь в группе 'client'
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Клиент').exists()

class IsGroupMember(BasePermission):
    # проверяет, состоит ли пользователь в группе 'group'
    def has_permission(self, request, view):
        return request.user.groups.filter(name='group').exists()