from rest_framework import serializers
from .models import Item, Order
#from .models import Order

class ItemSerializer(serializers.ModelSerializer):

   class Meta:
       model = Item
       fields = ('id', 'name', 'description', 'price', 'category',)

class OrderSerializer(serializers.ModelSerializer):   
   #items = serializers.StringRelatedField(many=True)   
   items = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
   class Meta:
         model = Order
         fields = ('id', 'user', 'items', 'date_created', 'order_total',)
   
   
 #why am I getting back item ids and not item names 
 #why am I being asked to enter order total?
 #why are my post requests not sending from react?