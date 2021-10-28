from django.shortcuts import render
from product.models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    length = len(Product.objects.all())
    return render(request, 'home/index.html', {'recent': products[length-3:length], 'famous': products.order_by('views')[length-3:length]})
