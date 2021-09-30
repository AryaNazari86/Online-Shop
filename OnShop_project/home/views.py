from django.shortcuts import render
from product.models import Product


# Create your views here.
def home(request):
    length = len(Product.objects.all())
    return render(request, 'home/index.html', {'recent_products': Product.objects.all()[length-3:length]})
