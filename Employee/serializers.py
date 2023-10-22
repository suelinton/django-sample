from rest_framework import serializers
from Employee.models import Employees

# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Departments
#         fields=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId','EmployeeName','EmployeeLastName','Department','DateOfJoining')

