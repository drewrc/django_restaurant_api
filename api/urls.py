from django.urls import path, include

urlpatterns = [
    path('items/', include('orders.urls')),
]