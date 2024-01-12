from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from core.models import Role, Status, Table, Category, Avoid, Extra, Ingredient, Employee, Plate, Transaction

from core.serializers import RoleSerializer, EmployeeSerializer, StatusSerializer, TableSerializer, CategorySerializer, AvoidSerializer, ExtraSerializer, IngredientSerializer, PlateSerializer, TransactionSerializer

# Create your views here.
class RoleListAPIView(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class StatusModelViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class TableModelViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AvoidModelViewSet(ModelViewSet):
    queryset = Avoid.objects.all()
    serializer_class = AvoidSerializer

class ExtraModelViewSet(ModelViewSet):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer

class IngredientModelViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class PlateModelViewSet(ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer

class TransactionModelViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
