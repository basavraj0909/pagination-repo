from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


class ProdViewset(viewsets.ModelViewSet):

    queryset = Product.objects.all().order_by('created_at')  # Order by created_at for cursor pagination
    serializer_class = ProductSerializer