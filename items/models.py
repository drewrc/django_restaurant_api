from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=30, default='category', editable=True)

    def __str__(self):
        return self.name