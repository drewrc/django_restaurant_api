from django.db import models
from django.conf import settings

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=30, default='category', editable=True)

    def __str__(self):
        return self.name

class Order(models.Model):

    user = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=8, decimal_places=2)
    items = models.ManyToManyField(Item, related_name='orders')
    # itemname = models.ManyToManyField(Item, related_name='order_names')
    def __str__(self):
        return f'Order {self.id}'



