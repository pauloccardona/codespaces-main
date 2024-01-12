from rest_framework import serializers
from core.models import Role, Employee, Status, Table, Category, Avoid, Extra, Ingredient, Plate, Transaction

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("id", "code","name")

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("code", "identifier", "name", "last_name", "role")

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ("id","name")

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ("code","name", "date", "status")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","name")

class AvoidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avoid
        fields = ("id","name")

class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = ("id","name", "price")

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("id","name", "price")

class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = ("category","name", "description", "ingredient", "price")


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("waithress",
                  "table",
                   "date",
                   "quantity",
                   "plate",
                   "avoid",
                   "extra",
                   "kitchenmessage"
                )