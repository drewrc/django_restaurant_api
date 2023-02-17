from rest_framework import serializers
from .models import Item, Order
#from .models import Order

class ItemSerializer(serializers.ModelSerializer):
   class Meta:
       model = Item
       fields = ('id', 'name', 'description', 'price', 'category',)

class OrderSerializer(serializers.ModelSerializer):
   items = serializers.StringRelatedField(many=True)
   class Meta:
      model = Order
      fields = ('id', 'user' 'items', 'date_created', 'order_total',)