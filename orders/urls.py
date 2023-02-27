from django.urls import path
from . import views

urlpatterns = [
   path('items/', views.ItemsListAPIView.as_view()),
   # path('orders/create/', views.OrderCreateAPIView.as_view()),
   path('orders/', views.OrderListCreateAPIView.as_view()),
]

