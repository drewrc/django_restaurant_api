# Create your views here

#from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

class ItemsListAPIView(generics.ListCreateAPIView):
   queryset = Item.objects.all()
   serializer_class = ItemSerializer