from rest_framework.permissions import BasePermission

class IsEmployee(BasePermission):
    # класс разрешений, который проверяет, состоит ли пользователь в группе
    def has_permission(self, request, view):
        return request.user.groups.filter(name='employee').exists()

class IsClient(BasePermission):
    # проверяет, состоит ли пользователь в группе 'client'
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Клиенты').exists()

class IsDirector(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Директор компании').exists()

class IsChiefEngineer(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Главный инженер').exists()

class IsSiteManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Прораб').exists()

class IsArchitect(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Архитектор').exists()

class IsEstimator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Сметчик').exists()

class IsDesigner(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Проектировщик').exists()

class IsEngineerPTO(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Инженер ПТО').exists()

class IsAccountant(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Бухгалтер').exists()

class IsLawyer(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Юрист').exists()

class IsSalesPurchasingManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Менеджер').exists()

class IsConstructionWorker(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Строительные рабочие').exists()

class IsSafetyOfficer(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Мастер по технике безопасности').exists()

class IsOccupationalSafetyEngineer(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Инженер по охране труда').exists()

class IsLogisticsSpecialist(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Специалист по логистике').exists()

class IsSurveyor(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Геодезист').exists()

class IsGroupMember(BasePermission):
    # проверяет, состоит ли пользователь в группе 'group'
    def has_permission(self, request, view):
        return request.user.groups.filter(name='group').exists()
