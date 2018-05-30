from rest_framework import permissions

from ..models import Employee


class IsStaff(permissions.BasePermission):
    """
    The request is authenticated as a user and has staff permission, or is a read-only request.
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and request.user.is_staff:
            return True
        return False


class IsOwner(permissions.BasePermission):
    """
    The request is authenticated as a user and profile owner, or is a read-only request.
    """

    def has_permission(self, request, view):
        employee = Employee.objects.get(pk=view.kwargs['pk'])
        if request.user == employee:
            return True
        return False
