from django.db.models import fields
from django.db import models
from rest_framework import serializers
from product.models import Product


class ProductAPI(serializers.ModelSerializer):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    phone_number = models.IntegerField()
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/products', default='images/default_product.png', blank=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['name', 'description', 'price', 'phone_number', 'city', 'image']
