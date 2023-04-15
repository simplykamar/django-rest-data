from django.shortcuts import render
from testapp.models import Employee
from rest_framework.viewsets import ModelViewSet
from testapp.serializers import EmployeeSerializer

# Create your views here.


class EmployeeCRUD(ModelViewSet):
	serializer_class=EmployeeSerializer
	queryset=Employee.objects.all()