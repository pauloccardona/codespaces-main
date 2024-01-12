from django.urls import path
from rest_framework import routers

from core import views

router = routers.SimpleRouter()

router.register(r'employees', views.EmployeeModelViewSet, basename= "Employee")
router.register(r'status', views.StatusModelViewSet, basename= "status")
router.register(r'tables', views.TableModelViewSet, basename= "table")
router.register(r'categories', views.CategoryModelViewSet, basename= "category")
router.register(r'avoids', views.AvoidModelViewSet, basename= "avoid")
router.register(r'extras', views.ExtraModelViewSet, basename= "extra")
router.register(r'ingredients', views.IngredientModelViewSet, basename= "ingredient")
router.register(r'plates', views.PlateModelViewSet, basename= "plate")
router.register(r'transactions', views.TransactionModelViewSet, basename= "transactions")


urlpatterns = [
    path("roles/", views.RoleListAPIView.as_view(), name="roles")
] + router.urls
