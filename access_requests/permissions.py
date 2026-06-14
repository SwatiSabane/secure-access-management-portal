from rest_framework.permissions import BasePermission


class IsEmployee(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'employee'


class IsManagerOrAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.role in ['manager', 'admin']