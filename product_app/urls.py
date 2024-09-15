from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdViewset


router = DefaultRouter()
router.register(r'products',ProdViewset)

urlpatterns = [
    path('', include(router.urls)),
]