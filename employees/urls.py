from rest_framework.routers import DefaultRouter

from employees.api import views as api

router = DefaultRouter()
router.register(r'api/employees', api.EmployeeModelViewSet)

urlpatterns = router.urls
