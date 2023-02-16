from django.urls import path
from . import views

urlpatterns = [
   path('', views.ItemsListAPIView.as_view()),
   #path('orders/', views.OrdersListAPIView.as_view()),
]

