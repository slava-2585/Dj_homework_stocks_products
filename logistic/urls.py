from django.urls import path
from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet, Sample_view

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)
#router.register('test', Sample_view)

urlpatterns = [
    router.urls,
    path('/api/v1/test', Sample_view),
]
