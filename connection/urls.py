from rest_framework.routers import DefaultRouter
from connection.views import PortsList

router = DefaultRouter()
router.register(r'connection', PortsList, basename='connection')

urlpatterns = router.urls
