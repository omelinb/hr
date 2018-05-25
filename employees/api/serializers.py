from rest_framework import serializers
from ..models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'rank', 'department', 'phone', 'first_name', 'last_name')
