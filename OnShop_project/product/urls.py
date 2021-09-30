from django.urls import path
from . import views

urlpatterns = [
    path('create_product/', views.create_product, name='create_product'),
    path('buy/<int:id>/', views.buy, name='buy'),
    path('search/', views.search, name='search'),
]