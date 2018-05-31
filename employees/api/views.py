from rest_framework import viewsets

from .serializers import EmployeeSerializer, OwnerSerializer
from .permissions import IsStaff, IsOwner
from ..models import Employee


class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsStaff]
        elif self.action in ['partial_update']:
            permission_classes = [IsOwner]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ['partial_update']:
            return OwnerSerializer
        return EmployeeSerializer
