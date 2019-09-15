from rest_framework import routers
from cAuth.api import LoginViewSet

router = routers.DefaultRouter()
router.register('api/auth',LoginViewSet,'auth')

urlpatterns = router.urls
  
