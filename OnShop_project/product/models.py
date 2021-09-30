from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    phone_number = models.IntegerField()
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/products', default='images/default_product.png', blank=True)

    def get_absolute_url(self):
        return reverse("buy", kwargs={"id": self.id})
