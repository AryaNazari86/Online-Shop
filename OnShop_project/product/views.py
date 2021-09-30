from django.shortcuts import render
from .models import Product
from .forms import ProductForm


# Create your views here.
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            length = len(Product.objects.all())
            product = form.save(commit=False)
            product.author = request.user.pk
            product = form.save()
            request.user.products.append(product.pk)
            return render(request, 'home/index.html', {'recent_products': Product.objects.all()[length - 2:length]})
    else:
        form = ProductForm()
        return render(request, 'product/create_product.html', {'form': form})


def buy(request, id):
    obj = Product.objects.get(id=id)
    return render(request, 'product/buy.html', {'obj': obj})


def search(request):
    search_value = request.GET['search_value'].lower()
    searched_products = filter(lambda x: search_value in x.name.lower(), Product.objects.all())
    return render(request, 'product/search.html', {'products': searched_products})
