from django.urls import path
from . import views

urlpatterns = [
    path('create_product/', views.create_product, name='create_product'),
    path('product_preview/<int:id>/', views.product_preview, name='product_preview'),
    path('search/', views.search, name='search'),
]