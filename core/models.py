from django.db import models

# Create your models here.

#PayRoll Models
class Role(models.Model):
    code = models.DecimalField(max_digits=3,decimal_places=2)
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    code = models.CharField(max_length=3, unique=True)
    identifier = models.DecimalField(max_digits=3,decimal_places=2)
    name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name="employees")

    def __str__(self):
        return self.name
    
#Restaurant Tables Related Models
class Status(models.Model):
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name

class Table(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=32, blank=True)
    date = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name="tables")

    def __str__(self):
        return self.name

#Plates Menu Related Models
class Category(models.Model):
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name
    
class Avoid(models.Model):
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name
    
class Extra(models.Model):
    name = models.CharField(max_length=32, blank=True)
    price = models.DecimalField(max_digits=3,decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.price}"

class Ingredient(models.Model):
    name = models.CharField(max_length=32, blank=True)
    price = models.DecimalField(max_digits=3,decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.price}"
    
class Plate(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, blank=True)
    description = models.CharField(max_length=32, blank=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, related_name="plates")
    price = models.DecimalField(max_digits=3,decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.description} {self.price}" 

#Transactions and Check Related Models
class Transaction(models.Model):
    waithress = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="transactions")
    table = models.ForeignKey(Table, on_delete=models.PROTECT, related_name="transactions")
    date = models.DateTimeField()
    quantity = models.DecimalField(max_digits=2,decimal_places=0)
    plate = models.ForeignKey(Plate, on_delete=models.SET_NULL, null=True, blank=True, related_name="plates")
    avoid = models.ForeignKey(Avoid, on_delete=models.PROTECT, related_name="transactions")
    extra = models.ForeignKey(Extra, on_delete=models.PROTECT, related_name="transactions")
    kitchenmessage = models.TextField(blank=True)

    def __str__(self):
        return f" {self.waithress} {self.table} {self.date} {self.plate.name} {self.avoids} {self.extras} {self.kitchenmessage} {self.plate.price}"

class Payment(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT, related_name="payments")
    forma = models.TextField(blank=True)
    status = models.TextField(blank=True)

    def __str__(self):
        return f" {self.transaction} {self.forma} {self.status}"
