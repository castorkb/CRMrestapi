from rest_framework.permissions import BasePermission

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='employee').exists()

class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='client').exists()

class IsGroupMember(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='group').exists()
