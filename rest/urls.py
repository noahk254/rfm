from rest_framework.routers import DefaultRouter
from .views import LivestockViewSet, EmployeeViewSet, SupplierViewSet

router = DefaultRouter()
router.register(r'livestock', LivestockViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'suppliers', SupplierViewSet)

urlpatterns = router.urls
