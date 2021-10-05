from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.db import transaction


# Create your views here.
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            length = len(Product.objects.all())
            product = form.save()
            print(product.owner)
            request.user.products.append(product.pk)
            return render(request, 'home/index.html', {'recent_products': Product.objects.all()[length - 2:length]})
    else:
        form = ProductForm()
        return render(request, 'product/create_product.html', {'form': form})


def product_preview(request, id):
    product = Product.objects.get(id=id)

    product.visited()
    transaction.commit()

    return render(request, 'product/product_preview.html', {'obj': product})


def search(request):
    search_value = request.GET['search_value'].lower()
    searched_products = filter(lambda x: search_value in x.name.lower(), Product.objects.all())
    return render(request, 'product/search.html', {'products': searched_products})
