# urls.py в приложении medcard
from rest_framework.routers import DefaultRouter
from .views import MedCardViewSet

router = DefaultRouter()
router.register(r'medcards', MedCardViewSet, basename='medcard')

urlpatterns = router.urls
