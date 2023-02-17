from django.shortcuts import render
from rest_framework import generics
from .models import Order, Item
from .serializers import ItemSerializer, OrderSerializer
#OrderSerializer

class ItemsListAPIView(generics.ListCreateAPIView):
   queryset = Item.objects.all()
   serializer_class = ItemSerializer

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Order.objects.all()
   serializer_class = OrderSerializer