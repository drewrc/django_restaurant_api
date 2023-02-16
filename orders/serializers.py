from rest_framework import serializers
from .models import Item
#from .models import Order

class ItemSerializer(serializers.ModelSerializer):
   class Meta:
       model = Item
       fields = ('id', 'name', 'description', 'price', 'category',)

#class OrderSerializer(serializers.ModelSerializer):
#    items = serializers.StringRelatedField(many=True)
#    class Meta:
#       model = Order
#       fields = ('id', 'items', 'date_created', 'ordered', 'order_total',)