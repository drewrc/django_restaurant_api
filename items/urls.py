from django.urls import path
from .views import ItemsListAPIView

urlpatterns = [
   path('', ItemsListAPIView.as_view())
]
