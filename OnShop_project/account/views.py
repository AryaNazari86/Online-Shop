from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView

User = get_user_model()


# Create your views here.
# Create your views here.
def create_product(request):
    submitted = False
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/index.html', {'recent_products': Product.objects.all()[length-2:length]})
    else:
        form = ProductForm()
        return render(request, 'product/create_product.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = User(request.POST)
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        city = request.POST['city']
        if 'image' in request.POST:
            image = request.POST['image']
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password,
                                     city=city, image=image)
        else:
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password,
                                     city=city)
        return render(request, 'account/signin.html')
    else:
        return render(request, 'account/signup.html')


class Signin(LoginView):
    redirect_field_name = 'account/profile.html'
    template_name = 'account/signin.html'


class Signout(LogoutView):
    template_name = 'account/signout.html'


def profile(request):
    return render(request, 'account/profile.html')
