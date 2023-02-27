from rest_framework import generics
from .models import Order, Item
from .serializers import ItemSerializer, OrderSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from collections import Counter



class ItemsListAPIView(generics.ListCreateAPIView):
   queryset = Item.objects.all()
   serializer_class = ItemSerializer

# class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Order.objects.all()
#    serializer_class = OrderSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def create_order(request):
    order_serializer = OrderSerializer(data=request.data)
    if order_serializer.is_valid():
        user = order_serializer.validated_data['user']
        item_ids = order_serializer.validated_data['items']
        items = Item.objects.filter(pk__in=item_ids)
        order_total = sum(item.price for item in items)
        order = Order.objects.create(user=user, order_total=order_total)
        item_id_counts = Counter(item_ids)
        for item_id, count in item_id_counts.items():
            for i in range(count):
                item = get_object_or_404(Item, pk=item_id)
                order.items.add(item)
        order_serializer = OrderSerializer(order)
        return JsonResponse(order_serializer.data, status=201)
    else:
        return JsonResponse(order_serializer.errors, status=400)



   #  def create_order(self, request):
   #      order_serializer = OrderSerializer(data=request.data)
   #      if order_serializer.is_valid():
   #          user = order_serializer.validated_data['user']
   #          items = order_serializer.validated_data['items']
   #          order_total = 0
   #          order = Order.objects.create(user=user)
   #          for item_id in items:
   #              item = get_object_or_404(Item, pk=item_id)
   #              order.items.add(item)
   #              order_total += item.price
   #          order.order_total = order_total
   #          order.save()
   #          return JsonResponse(order_serializer.data, status=201)
   #      else:
   #          return JsonResponse(order_serializer.errors, status=400)

   #  def post(self, request, *args, **kwargs):
   #      return self.create_order(request)

   # def create_order(request):
   #    order_serializer = OrderSerializer(data=request.data)
   #    if order_serializer.is_valid():
   #       user = order_serializer.validated_data['user']
   #       item_ids = order_serializer.validated_data['items']
   #       order_total = 0
   #       order = Order.objects.create(user=user)
   #       for item_id in item_ids:
   #             item = get_object_or_404(Item, pk=item_id)
   #             order.items.add(item)
   #             order_total += item.price
   #       order.order_total = order_total
   #       order.save()
   #       return JsonResponse(order_serializer.data, status=201)
   #    else:
   #       return JsonResponse(order_serializer.errors, status=400)
# class OrderCreateAPIView(generics.CreateAPIView):
#    queryset = Order.objects.all()
#    serializer_class = OrderSerializer


