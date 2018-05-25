from django.urls import re_path, include

from rest_framework.routers import DefaultRouter

from employees.api import views as api

router = DefaultRouter()
router.register(r'api/employees', api.EmployeeViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls))
]
