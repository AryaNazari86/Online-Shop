from django.urls import path
from . import views

urlpatterns = [
    path('productlist', views.ProductList.as_view(), name='productlist'),
]