from rest_framework.generics import ListCreateAPIView
from . import serializers
from product.models import Product


# Create your views here.
class ProductList(ListCreateAPIView):
    serializer_class = serializers.ProductAPI
    queryset = Product.objects.all()
