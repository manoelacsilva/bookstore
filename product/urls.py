from django.urls import include, path
from rest_framework import routers

from product import viewsets

router = routers.SimpleRouter()
router.register(r"product", viewsets.ProductViewSet, basename="product")


urlpatterns = [
    path("", include(router.urls)),
]