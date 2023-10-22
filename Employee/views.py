from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Employee.models import Employees
from Employee.serializers import EmployeeSerializer
# Create your views here.


@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        dep = Employees.objects.all()
        dep_serializer=EmployeeSerializer(dep,many=True)
        return JsonResponse(dep_serializer.data, safe=False)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Add sucssfull", safe=False)
        return JsonResponse("FAILED", safe=False)
    elif request.method=='PUT':
        data=JSONParser().parse(request)
        department = Employees.objects.get(DepartmentId=data['DepartmentId'])
        serializer=EmployeeSerializer(department, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update sucssfull", safe=False)
        return JsonResponse("FAILED", safe=False)
    elif request.method=='DELETE':
        department=Employees.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Succ", safe=False)